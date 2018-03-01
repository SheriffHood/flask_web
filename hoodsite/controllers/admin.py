#!usr/bin/env python3
#-*- coding:utf-8 -*-

from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import current_user, login_required
from hoodsite.extensions import admin_permission

class CustomView(BaseView):
    
    @expose('/')
    @login_required
    @admin_permission.require(http_exception=403)
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    @login_required
    @admin_permission.require(http_exception=403)
    def second_page(self):
        return self.render('admin/second_page.html')

class CustomModelView(ModelView):
    
    def is_accessible(self):
        return current_user.is_authenticated and admin_permission.can()

class CustomFileAdmin(FileAdmin):
    
    def is_accessible(self):
        return current_user.is_authenticated and admin_permission.can()

class UserView(ModelView):
    can_delete = False

class PostView(ModelView):
    page_size = 20
    column_searchable_list = ('text', 'title')
    column_filters = ('title',)

    edit_template = 'admin/post_edit.html'
