# -*- coding: UTF-8 -*-
"""
사이트 운영에 필요한 기본 설정 내역
"""
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' #암호화 키
BCRYPT_LEVEL = 1
IV = 'BBBBBBBBBBBBBBBB' #암호화 IV
#DATABASE_URI = 'sqllite:///' + os.path.join(_basedir, 'website.db')
DATABASE_URI = os.path.join(_basedir,'website.db')
COOKIE_NAME = 'FWHK'
JSON_AS_ASCII = False

del os