# -*- coding: UTF-8 -*-
import os
import unittest
import pyaes
import base64

class pyseTestCase(unittest.TestCase):
    def setUp(self):
        self.key = 'C4B79F711872474BA780F593FB7B0B36' #32
        self.iv = 'C4B79F711872474B' #16

    def test_pyase(self):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        plaintext = '{"id": "222", "password": "33", "seq": 0}'
        ciphertext = aes.encrypt(plaintext)

        text = base64.b16encode(ciphertext)
        print text

        aes = pyaes.AESModeOfOperationCTR(self.key)
        decrypted = aes.decrypt(base64.b16decode(text))

        print decrypted
        print decrypted == plaintext

