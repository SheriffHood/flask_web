#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
Date: 2017-12-7
Author: yuexing
Keyword: define database 
'''

from flask_sqlalchemy import SQLAlchemy
from hood_site import app

db = SQLAlchemy(app)

class User(db.Model):
    '''user class'''

    __tablename__ = 'users'

    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='users', lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    '''post class'''

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime)
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))


    def __init__(self, title):
        self.title = title

    def __repr__():
        return '<Model Post %r>' % self.title
