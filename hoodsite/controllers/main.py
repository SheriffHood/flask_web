#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from os import path
from uuid import uuid4

from flask import flash, url_for, redirect, render_template, Blueprint
from flask_login import login_user, logout_user
from flask_principal import Principal, Identity, identity_changed, current_app, AnonymousIdentity
from hoodsite.forms import LoginForm, RegisterForm
from hoodsite.models import User, db

main_blueprint = Blueprint('main', __name__, template_folder=path.join(path.pardir, 'templates', 'main'))

@main_blueprint.route('/')
def index():
    return redirect( url_for('blog.home') )

@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user, remember=form.remember.data)
        identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
        flash("You have logined in", category="success")
        return redirect(url_for('blog.home'))

    return render_template('login.html', form=form)

@main_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():

    logout_user()
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    flash("You have logged out", category="success")
    return redirect(url_for('main.login'))

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(id=str(uuid4()), username=form.username.data, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash("Your user has been created, please login", category="success")
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)
