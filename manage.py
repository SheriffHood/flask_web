#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os

from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand
from hoodsite import create_app
from hoodsite.models import db, User, Post, Comment, Tag

env = os.environ.get('BLOG_ENV', 'dev')

app = create_app('hoodsite.settings.%sConfig' % env.capitalize())

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, Tag=Tag)

if __name__ == '__main__':
    manager.run()
