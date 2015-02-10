# coding: utf-8

from datetime import datetime
from google.appengine.api import app_identity
#import model
import os


PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Eng')
DEVELOPMENT = not PRODUCTION
DEBUG = DEVELOPMENT

CURRENT_VERSION_ID = os.environ.get('CURRENT_VERSION_ID')
CURRENT_VERSION_NAME = CURRENT_VERSION_ID.split('.')[0]
CURRENT_VERSION_TIMESTAMP = long(CURRENT_VERSION_ID.split('.')[1]) >> 28
if DEVELOPMENT:
    import calendar
    CURRENT_VERSION_TIMESTAMP = calendar.timegm(datetime.utcnow().timetuple())
CURRENT_VERSION_DATE = datetime.utcfromtimestamp(CURRENT_VERSION_TIMESTAMP)
APPLICATION_ID = app_identity.get_application_id()

#CONFIG_DB = model.Config.get_master_db()
#SECRET_KEY = CONFIG_DB.flask_secret_key.encode('ascii')
