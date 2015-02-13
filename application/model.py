# coding: utf-8

from google.appengine.ext import ndb

import config
import modelx


class Base(ndb.Model, modelx.BaseX):
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)
    version = ndb.IntegerProperty(default=config.CURRENT_VERSION_TIMESTAMP)

    _PROPERTIES = {
        'key',
        'id',
        'version',
        'created',
        'modified',
    }


class Item(Base, modelx.ItemX):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty(required=True)
    catagory = ndb.StringProperty(required=True)


