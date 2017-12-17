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

class ProdConfig(object):
    '''
    Production Config Class
    '''
    pass

class DevConfig(object):
    '''
    Development Config Class
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/hoodsite'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
