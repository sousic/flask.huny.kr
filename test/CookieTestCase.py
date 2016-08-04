# -*- coding: UTF-8 -*-
import unittest
import website
from website.Cookies import Cookies


class CookieTestCase(unittest.TestCase):
    def setUp(self):
        self.userid = 'test'
        website.app.config['TESTING'] = True
        self.app = website.app.test_client()
        self.Cookies = Cookies

    def test_setcookie(self):
        self.Cookies.setCookie('site', 'test')

    def test_getcooike(self):
        cookies = self.Cookies.getCookie('site')
        assert cookies in 'test'

if __name__ == '__main__':
    unittest.main()