# -*- coding: UTF-8 -*-
import sqlite3
from flask import _app_ctx_stack

class commonDAO:
    def __init__(self, app):
        self.app = app

    def get_db(self):
        top = _app_ctx_stack.top
        if not hasattr(top, 'sqlite_db'):
            print self.app.config['DATABASE_URI']
            print 'db open'
            top.sqlite_db = sqlite3.connect(self.app.config['DATABASE_URI'])
            return top.sqlite_db

    def close_connection(self, exception):
        top = _app_ctx_stack.top
        if hasattr(top, 'sqlite_db'):
            top.sqlite_db.close()
            print 'db close'