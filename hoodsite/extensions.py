#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_principal import Principal, Permission, RoleNeed
from flask_celery import Celery
from flask_mail import Mail
from flask_cache import Cache
from flask_assets import Environment, Bundle
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect

bcrypt = Bcrypt()
login_manager = LoginManager()
principals = Principal()
flask_celery = Celery()
mail = Mail()
cache = Cache()
assets = Environment()
flask_admin = Admin()
csrf = CSRFProtect()

login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"

admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))

main_css = Bundle('css/bootstrap.css', 'css/bootstrap-theme.css', filters='cssmin', output='assests/css/common.css')
main_js = Bundle('js/bootstrap.css', filters='jsmin', output='assets/js/common.js')

@login_manager.user_loader
def load_user(user_id):
    
    from hoodsite.models import User
    return User.query.filter_by(id=user_id).first()
