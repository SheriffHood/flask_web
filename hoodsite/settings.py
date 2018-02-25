'''
Author: yuexing
Date: 2017-12-04
Keyword: config files
'''

class Config(object):
    '''
    Base Config Class
    '''
    SECRET_KEY = 'cf7fb7e99f88ebcba48385827c810882'
    CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672//'
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'

class ProdConfig(Config):
    '''
    Production Config Class
    '''
    pass

class DevConfig(Config):

    '''
    Development Config Class
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/hoodsite'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CACHE_TYPE = 'simple'
