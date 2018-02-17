#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
Date: 2017-12-7
Author: yuexing
Keyword: define database 
'''
from flask_sqlalchemy import SQLAlchemy
from hoodsite.extensions import bcrypt

db = SQLAlchemy()

posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))

users_roles = db.Table('users_roles',
    db.Column('user_id', db.String(45), db.ForeignKey('users.id')),
    db.Column('role_id', db.String(45), db.ForeignKey('roles.id')))

class User(db.Model):
    '''user class'''

    __tablename__ = 'users'

    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='users', lazy='dynamic')
    roles = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        return bcrypt.generate_password_hash(password, 10)

    def check_password(self, password):
        return bcrypt.check_password_hash(bcrypt.generate_password_hash(password, 10), password)

    def is_authenticated(self):
        if isinstance(self, AnonymouseUserMixin):
            return False
        else:
            return True

    def is_active():
        return True

    def is_anonymouse(self):
        if isinstance(self,AnonymouseUserMixin):
            return True
        else:
            return False    

    def get_id(self):
        return (self.id)

class Role(db.Model):
    '''Protected roles'''

    __tablename__ = 'roles'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255),unique=True)
    description = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Model Role %r>' % self.name

class Post(db.Model):
    '''post class'''

    __tablename__ = 'posts'

    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='posts', lazy='dynamic')
    tags = db.relationship('Tag', secondary=posts_tags, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return '<Model Post %r>' % self.title

class Comment(db.Model):
    '''comment class'''

    __tablename__ = 'comments'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Comment %r>' % self.name

class Tag(db.Model):
    '''tag class'''

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return '<Model Tag %r>' % self.name
