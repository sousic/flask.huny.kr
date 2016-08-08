# -*- coding: UTF-8 -*-
import base64
import pyaes
from werkzeug.utils import redirect

import websiteconfig


class CookieHelper(object):
    def init_app(self, app):
        self.app = app
        self.app.cookie_helper = self

    def SetCookies(self, response, user):
        aes = pyaes.AESModeOfOperationCTR(websiteconfig.SECRET_KEY)
        chiphertext = aes.encrypt(user.to_json())
        response.set_cookie('FWHK', base64.b16encode(chiphertext))

    @classmethod
    def GetCookies(self, request):
        if request is not None:
            cookies = base64.b16decode(request.cookies.get('FWHK'))
            aes = pyaes.AESModeOfOperationCTR(websiteconfig.SECRET_KEY)
            decrpyted = aes.decrypt(cookies)
            return decrpyted
        else:
            return None

    def CheckCookie(self,f):
        print 'decorator'
        f()