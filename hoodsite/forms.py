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

    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")

    def validate(self):

        check_validata = super(LoginForm, self).validate

        if not check_validata:
            return False

        user = User.query.filter_by(username=self.username.data).first()

        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True

class RegisterForm(FlaskForm):
    """Register Form"""

    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    username = StringField('Username', [DataRequired(), Length(max=25)])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])

    def validate(self):

        check_validata = super(RegisterForm, self).validate
        
        if not check_validata:
            return False

        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username already in use')

        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email already registered')

        return True

class PostForm(FlaskForm):
    """Post Form"""
    
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired()])
