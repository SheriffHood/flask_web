#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask
from settings import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

views = __import__('views')

if __name__ == '__main__':
    app.run()
