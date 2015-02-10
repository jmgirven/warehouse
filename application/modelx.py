# coding: utf-8

import flask


class BaseX(object):
    @classmethod
    def retrieve_one_by(cls, name, value):
        return cls.query(getattr(cls, name) == value).get()


class ItemX(object):
    @property
    def test_property(self):
        return None

