#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_principal import Principal, Permission, RoleNeed
from flask_celery import Celery
from flask_mail import Mail
from flask_cache import Cache

bcrypt = Bcrypt()
login_manager = LoginManager()
principals = Principal()
flask_celery = Celery()
mail = Mail()
cache = Cache()

login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"

admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))

@login_manager.user_loader
def load_user(user_id):
    
    from hoodsite.models import User
    return User.query.filter_by(id=user_id).first()
