#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask
from settings import DevConfig
import wt_forms
import views

app = Flask(__name__)
app.config.from_object(DevConfig)


if __name__ == '__main__':
    app.run()
