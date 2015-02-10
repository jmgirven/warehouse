# coding: utf-8
"""
Initialize Flask app

Inspiration from: https://github.com/kamalgill/flask-appengine-template
"""

__author__ = 'j.m.girven@gmail.com (Jonathan Girven)'

import datetime
from flask import Flask
import os

import config

app = Flask('application')

if config.PRODUCTION and os.getenv('FLASK_CONF') == 'PROD':
    app.config.from_object('application.settings.Production')

elif config.PRODUCTION:
    app.config.from_object('application.settings.Testing')
else:
    if os.getenv('FLASK_CONF') == 'DEV':
        #development settings
        app.config.from_object('application.settings.Development')

    elif os.getenv('FLASK_CONF') == 'PROD' or os.getenv('FLASK_CONF') == 'TEST':
        app.config.from_object('application.settings.Testing')

    else:
        app.config.from_object('application.settings.Production')

# Pull in URL dispatch routes
import urls
