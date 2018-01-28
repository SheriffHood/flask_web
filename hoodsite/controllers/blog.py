#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import render_template, Blueprint, redirect, url_for
from uuid import uuid4
from os import path
from datetime import datetime
from sqlalchemy import func
from hoodsite.models import db, User, Post, Comment, Tag, posts_tags
from hoodsite.forms import CommentForm, PostForm


blog_blueprint = Blueprint('blog',
                            __name__,
                            template_folder=path.join(path.pardir, 'templates', 'blog'),
                            url_prefix='/blog')

def sidebar_data():
    recent = db.session.query(Post).order_by(Post.publish_date.desc()).limit(5).all()

    top_tags = db.session.query(Tag, 
    func.count(posts_tags.c.post_id).label('total')).join(posts_tags).group_by(Tag).order_by('total Desc').limit(5).all()

    return recent, top_tags

@blog_blueprint.route('/')
@blog_blueprint.route('/<int:page>')
def home(page=1):
    '''view function for home page'''

    posts = Post.query.order_by(
        Post.publish_date.desc()
        ).paginate(page, 10)

    recent, top_tags = sidebar_data()

    return render_template('home.html',
                            posts=posts,
                            recent=recent,
                            top_tags=top_tags)

@blog_blueprint.route('/post/<string:post_id>', methods=('GET', 'POST'))
def post(post_id):
    '''view function for post page'''

    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(id=str(uuid4()), name=form.name.data)
        new_comment.text = form.text.data
        new_comment.date = datetime.datetime.now()
        new_comment.post_id = post_id
        db.session.add(new_comment)
        db.session.commit()

    post = db.session.query(Post).get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('post.html',
                            post=post,
                            tags=tags,
                            comments=comments,
                            recent=recent,
                            top_tags=top_tags,
                            form=form)

@blog_blueprint.route('/tag/<string:tag_name>')
def tag(tag_name):
    '''view function for tag page'''

    tag = db.session.query(Tag).filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('tag.html',
                            tag=tag,
                            posts=posts,
                            recent=recent,
                            top_tags=top_tags)

@blog_blueprint.route('/user/<string:username>')
def user(username):
    '''view function for user page'''

    user = db.session.query(User).filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data

    return render_template('user.html',
                            user=user,
                            posts=posts,
                            recent=recent,
                            top_tags=top_tags)

@blog_blueprint.route('/new', methods=['GET', 'POST'])
def new_post():
    
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(id=str(uuid4()), title=form.title.data)
        new_post.text = form.text.data
        new_post.publist_data = datetime.now()

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('blog.home'))

    return render_template('new_post.html', form=form)

@blog_blueprint.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit_post(id):
    
    post = Post.query.get_or_404(id)
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.publish_date = datetime.now()

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('blog.post', post_id=post.id))

    form.title.data = post.title
    form.text.data = post.text
    return render_template('edit_post.html', form=form, post=post)
