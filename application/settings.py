"""
settings.py

Configuration for Flask app

Important: Place your keys in the secret_keys.py module,
           which should be kept out of version control.

"""

import datetime
import os

from secret_keys import CSRF_SECRET_KEY, SESSION_KEY

class Config(object):
    # Set secret keys for CSRF protection
    SECRET_KEY = CSRF_SECRET_KEY
    CSRF_SESSION_KEY = SESSION_KEY
    # Other
    PERMANENT_SESSION_LIFETIME=datetime.timedelta(days=31)

class Development(Config):
    DEBUG = True
    # Flask-DebugToolbar settings
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CSRF_ENABLED = True
    MINIFIED = False
    SSL = False

class Testing(Config):
    TESTING = True
    DEBUG = True
    CSRF_ENABLED = True
    MINIFIED = False
    SSL = False

class Production(Config):
    DEBUG = False
    CSRF_ENABLED = True
    MINIFIED = True
    SSL = True