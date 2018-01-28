#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, TextAreaField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, URL
from hoodsite.models import User

class CommentForm(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    text = TextField(u'Comment', validators=[DataRequired()])

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('Username', [ Datarequired(), Length(max=255) ])
    password = PasswordField('Password',[Datarequired()])

    def validate(self):

        check_validata = super(LoginForm, self).validate

        if not check_validata:
            return False

        user = User.query.filter_by(username=self.data).first()

        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True

class RegisterForm(FlaskForm):
    """Register Form"""

    username = StringField('Username', [Datarequired(), Length(max=25)])
    password = PasswordField('Password', [Datarequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password', [Datarequired(), EqualTo('password')])

    def validate(self):

        check_validata = super(RegisterForm, self).validate
        
        if not check_validata:
            return False

        user = User.query.filter_by(username=self.data).first()
        if user:
            self.username.errors.append('User with that name already exists')
            return False

        return True
