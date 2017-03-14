#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'HOST'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return render_template('login.html', username=username)
        else:
            error = 'Invalid username/password'

    return render_template('form.html', error=error)

if __name__ == '__main__':
    app.run()
