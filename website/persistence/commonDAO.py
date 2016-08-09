# -*- coding: UTF-8 -*-
import sqlite3

class commonDAO:
    def __init__(self, app):
        self.app = app

    def connection_db(self):
        self.sqlite_db = sqlite3.connect(self.app.config['DATABASE_URI'])
        self.sqlite_db

    def disconnection_db(self):
        self.sqlite_db.close()

    def executeQuery(self, querys, args=(), one=False):
        self.connection_db()
        cur = self.sqlite_db.execute(querys, args)
        rs = cur.fetchall()
        cur.close()
        self.disconnection_db()
        return (rs[0] if rs else None) if one else rs

    def insertQuery(self, querys, args=(), one=False):
        self.connection_db()
        cur = self.sqlite_db.execute(querys, args)
        self.sqlite_db.commit()
        cur.close()
        self.disconnection_db()
