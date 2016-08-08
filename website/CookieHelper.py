# -*- coding: UTF-8 -*-
import base64
from functools import wraps

import pyaes
from flask import url_for, request, make_response
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


    def GetCookies(self, request):
        if request is not None:
            decrypted = request.cookies.get('FWHK')
            if decrypted is not None:
                cookies = base64.b16decode(decrypted)
                aes = pyaes.AESModeOfOperationCTR(websiteconfig.SECRET_KEY)
                decrpyted = aes.decrypt(cookies)
                return decrpyted
            else:
                return None
        else:
            return None

    #쿠키 체크 decorator
    def CheckCookie(self,f):
        @wraps(f)
        def _check_cookie_(*arg, **kwargs):
            cookie = self.GetCookies(request)
            if cookie is None:
                return redirect('/')
            return f(*arg, **kwargs)
        return _check_cookie_
