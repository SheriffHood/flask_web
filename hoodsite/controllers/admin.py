#!usr/bin/env python3
#-*- coding:utf-8 -*-

from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView

class CustomModelView(ModelView):
    pass

class UserView(ModelView):
    can_delete = False

class PostView(ModelView):
    page_size = 20
