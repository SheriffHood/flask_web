#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
Date: 2017-12-7
Author: yuexing
Keyword: define database 
'''
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, session
from flask_sqlalchemy import SQLAlchemy
from hoodsite.extensions import bcrypt, cache

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

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'confirm': self.id})
        
    @staticmethod
    @cache.memoize(60)
    def confirm_user(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        
        user = User.query.filter_by(id=data['id']).first()
        return user

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
    user = db.relationship('User', back_populates='posts')
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

class Reminder(db.Model):
    '''Mail class'''

    __tablename__ = 'reminders'
    id = db.Column(db.String(45), primary_key=True)
    date = db.Column(db.DateTime())
    email = db.Column(db.String(255))
    text = db.Column(db.Text())

    def __init__(self, id, text):
        self.id = id
        self.text = text

    def __repr__(self):
        return '<Model Reminder %r>' % self.text[:20]
