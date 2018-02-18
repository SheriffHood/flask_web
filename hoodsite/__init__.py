#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask, redirect, url_for
from flask_login import current_user
from flask_principal import identity_loaded, RoleNeed, UserNeed
from sqlalchemy import event
from hoodsite.models import db
from hoodsite.controllers import blog, main
from hoodsite.extensions import bcrypt, login_manager, principals, flask_celery, mail
from hoodsite.tasks import on_reminder_save


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)
    flask_celery.init_app(app)
    mail.init_app(app)
    
    @app.route('/')
    def index():
        return redirect( url_for('blog.home') )

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        identity.user = current_user

        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    event.listen(Reminder, 'after_insert', on_reminder_save)

    return app
