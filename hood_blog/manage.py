#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask.ext.script import Manager, Server
import hood_site
import models

manager = Manager(hood_site.app)

manager.add_command('server', Server())

@manager.shell
def make_shell_context():
    return dict(app=hood_site.app,
                db=models.db,
                User=models.User)

if __name__ == '__main__':
    manager.run()
