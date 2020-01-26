import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
        '''
        Base config class
        '''
        DEBUG = True
        TESTING = False
        SECRET_KEY = 'this-really-needs-to-be-changed'
        # DATABASE_URL = os.environ['DATABASE_URL']
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