#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length

class CommentForm(Form):
    
    name = StringField(validators=[DataRequired(), Length(max=255)])
    text = TextField(u'Comment', validators=[DataRequired()])
