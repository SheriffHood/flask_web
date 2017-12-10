#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import render_template
from sqlalchemy import func

from hood_site import app
from models import User, Post, Comment, Tag, posts_tags

def sidebar_data():
    recent = db.session.query(Post).order_by(Post.publist_date.desc()).limit(5).all()

    top_tags = db.session.query(Tag, 
    func.count(posts_tags.c.post_id).label('total')).join(posts_tags).group_by(Tag).order_by('total Desc').limit(5).all()

    return recent, top_tags
