# -*- coding: UTF-8 -*-
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'testkey'
DATABASE_URI = 'sqllite:///' + os.path.join(_basedir, 'website.db')

del os