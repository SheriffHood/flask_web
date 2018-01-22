#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask, redirect, url_for
from models import db
from settings import DevConfig
from controllers import blog

app = Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)

@app.route('/')
def index():
    return redirect( url_for('blog.home') )

app.register_blueprint(blog.blog_blueprint)

if __name__ == '__main__':
    app.run()
