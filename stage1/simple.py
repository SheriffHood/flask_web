#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask import abort
from flask import redirect
from flask import url_for

app = Flask(__name__)
app.config.from_object('config')

@app.route('/people/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return('Name: {0}; UA: {1}'.format(name, user_agent))

@app.route('/login/', methods=['GET, POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return('User: {} login'.format(user_id))
    else:
        return('Open Login Page')

@app.route('/secret/')
def secret():
    abort(401)
    print('This is never executed')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=app.debug)
