#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
Author: yuexing
Date: 2017-11-16
Keyword: redering templates
'''

from flask import Flask
from flask import render_template


app = Flask(__name__)
views = __import__('views')

app.add_url_rule('/index', view_func=views.index)
app.add_url_rule('/sayHello', view_func=view.sayHello)

if __name__ == '__main__':
    app.run(debug=True)
