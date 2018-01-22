#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask, redirect, url_for
from hoodsite import models
from hoodsite.controllers import blog


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    models.db.init_app(app)
    
    @app.route('/')
    def index():
        return redirect( url_for('blog.home') )

    app.register_blueprint(blog.blog_blueprint)

    return app
