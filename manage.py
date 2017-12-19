#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand
import hood_site
import models

manager = Manager(hood_site.app)
migrate = Migrate(hood_site.app, models.db)

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=hood_site.app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag)

if __name__ == '__main__':
    manager.run()
