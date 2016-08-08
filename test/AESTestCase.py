# -*- coding: UTF-8 -*-
import unittest

from website.AESCipher import AESCipher


class AESTestCase(unittest.TestCase):
    def setUp(self):
        self.key = 'eyJpZCI6ICIxMTIyMiIsICJwYXNzd29yZCI6ICIyMjIyIiwgInNlcSI6IDB9' #'abcdefghijklmnopqrstuvwxyz123456'
        self.mssage = u'한글을 테스트 합니다.'
        self._enc = 'gOXlygE+qxS+69zN5qC6eKJvMiEoDQtdoJb3zjT8f/E='

    def test_ase(self):
        enc = AESCipher(self.key).encrypt(self.mssage)
        dec = AESCipher(self.key).decrypt(self._enc)

        assert self.mssage in dec

if __name__ == '__main__':
    unittest.main()