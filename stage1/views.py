#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from hello import app

def index():
    return render_template('home.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def sayHello(name=None):
    return render_template('hello.html', name=name)
