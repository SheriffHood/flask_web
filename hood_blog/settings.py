'''
Author: yuexing
Date: 2017-12-04
Keyword: config files
'''

class Config(object):
    '''
    Base Config Class
    '''
    pass

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
    SQLALCHEMY_DATABASE_URI = 'mysql+mysql.connector://hoodsite.db'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
