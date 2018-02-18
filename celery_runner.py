#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
from celery import Celery
from hoodsite import create_app

def make_celery(app):

    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CECERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):

        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

env = os.environ.get('BLOG_ENV', 'dev')
flask_app = create_app('hoodsite.settings.%sConfig' % env.capitalize())
celery = make_celery(flask_app)
