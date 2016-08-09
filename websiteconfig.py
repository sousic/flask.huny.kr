# -*- coding: UTF-8 -*-
"""
사이트 운영에 필요한 기본 설정 내역
"""
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
BCRYPT_LEVEL = 1
IV = 'BBBBBBBBBBBBBBBB'
#DATABASE_URI = 'sqllite:///' + os.path.join(_basedir, 'website.db')
DATABASE_URI = os.path.join(_basedir,'website.db')
COOKIE_NAME = 'FWHK'
JSON_AS_ASCII = False

del os