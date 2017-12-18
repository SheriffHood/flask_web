#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask, redirect
from settings import DevConfig

app = Flask(__name__)

views = __import__('views')

app.config.from_object(DevConfig)

@app.route('/')
def index()
    return redirect(url_for('blog.home'))

if __name__ == '__main__':
    app.register_blueprint(blog_blueprint)
    app.run()
