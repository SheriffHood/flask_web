#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask, redirect, url_for
from hoodsite.models import db
from hoodsite.controllers import blog, main
from hoodsite.extensions import bcrypt, login_manager


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    @app.route('/')
    def index():
        return redirect( url_for('blog.home') )

    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    return app
