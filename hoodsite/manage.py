#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand
import main
import models

manager = Manager(main.app)
migrate = Migrate(main.app, models.db)

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=main.app, db=models.db, User=models.User, Post=models.Post, Comment=models.Comment, Tag=models.Tag)

if __name__ == '__main__':
    manager.run()
