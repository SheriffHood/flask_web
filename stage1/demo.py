#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
Author: Yuexing
Date: 2017-11-07
Keyword:
'''

from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/item/1')
def item(id):
    pass

with app.test_request_context() as a:
    print( url_for('item', id='1') )
    print( url_for('item', id='2', next='/') )
