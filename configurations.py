import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
        '''
        Base config class
        '''
        DEBUG = True
        TESTING = False
        SECRET_KEY = 'this-really-needs-to-be-changed'
        #export DATABASE_URL=$(heroku config:get DATABASE_URL -a testforsuccess-api)
        #sometimes it fails on the web, use Heroku CLI:
        #heroku ps:scale web=1 -a testforsuccess-api
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
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