#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from os import path
from uuid import uuid4

from flask import flash, url_for, redirect, render_template, Blueprint
from hoodsite.forms import LoginForms, RegisterForm
from hoodsite.models import User, db

main_blueprint = Blueprint('main', __name__, template_folder=path.join(path.pardir, 'templates', 'main'))

@main_blueprint.route('/')
def index():
    return redirect( url_for('blog.home') )
