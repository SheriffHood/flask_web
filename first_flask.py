#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from flask import Flask
from flask import abort
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def sayHello(name):
    if name == 'baidu':
        return redirect('http://www.baidu.com')
    elif name == 'NO':
        return abort(404)

    return '<h1>Hello  %s</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
