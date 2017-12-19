#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask, redirect, url_for
from settings import DevConfig
from models import db
from controllers import blog

app = Flask(__name__)
app.config.from_object(DevConfig)

'''undefined func'''
db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('blog.home'))

app.register_blueprint(blog_blueprint)

if __name__ == '__main__':
    app.run()
