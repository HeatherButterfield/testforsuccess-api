import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
        '''
        Base config class
        '''
        DEBUG = True
        TESTING = False
        SECRET_KEY = 'this-really-needs-to-be-changed'
        #export SQLALCHEMY_DATABASE_URI=$(heroku config:get DATABASE_URL -a testforsuccess-api)
        SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
        SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProductionConfig(BaseConfig):
        """
        Production specific config
        """
        DEBUG = False
class DevelopmentConfig(BaseConfig):
        """
        Development environment specific configuration
        """
        DEBUG = True
        TESTING = True