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
    __tablename__ = 'users'

    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>'.format(self.username)
