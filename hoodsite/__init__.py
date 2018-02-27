#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
from flask import Flask, redirect, url_for, session
from flask_login import current_user
from flask_principal import identity_loaded, RoleNeed, UserNeed
from sqlalchemy import event
from hoodsite.models import db, User, Post, Tag, Role, Reminder
from hoodsite.controllers import blog, main, admin
from hoodsite.extensions import bcrypt, login_manager, principals, flask_celery, mail, assets, cache, main_css, main_js, flask_admin
from hoodsite.tasks import on_reminder_save
from hoodsite.models import Reminder

def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)
    flask_celery.init_app(app)
    mail.init_app(app)
    assets.init_app(app)
    cache.init_app(app)
    flask_admin.init_app(app)

    flask_admin.add_view(admin.UserView(User, db.session))
    flask_admin.add_view(admin.PostView(Post, db.session))
    flask_admin.add_view(admin.CustomView(name='Custom'))

    path = os.path.join(os.path.dirname(__file__), 'static')
    flask_admin.add_view(admin.CustomFileAdmin(path, '/static/', name='Static Files'))

    models = [Role, Tag, Reminder]
    for model in models:

        flask_admin.add_view( admin.CustomModelView(model, db.session, category='Models') )
    
    assets.register('main_css', main_css)
    assets.register('main_js', main_js)

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
