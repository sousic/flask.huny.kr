# -*- coding: UTF-8 -*-
import unittest

import bcrypt
from flask import Flask

class BcrpytTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'I am your father'
        app.config['BCRYPT_LEVEL'] = 1

    def test_bcrpyt(self):
        strUserID = 'TEST'

        pw_hash =  bcrypt.hashpw(strUserID, bcrypt.gensalt())
        print pw_hash

        if bcrypt.hashpw(strUserID,pw_hash) == pw_hash:
            print 'ok', strUserID
        else:
            print 'fail', strUserID

if __name__ == '__main__':
    unittest.main()