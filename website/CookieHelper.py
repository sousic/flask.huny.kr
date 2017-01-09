# -*- coding: UTF-8 -*-
import base64
from functools import wraps

import pyaes
from flask import request
from werkzeug.utils import redirect

from website.domain.UserVO import UserVO


class CookieHelper(object):
    def init_app(self, app):
        self.app = app
        self.app.cookie_helper = self

    def SetCookies(self, response, user):
        aes = pyaes.AESModeOfOperationCTR(self.app.config['SECRET_KEY'])
        chiphertext = aes.encrypt(user.to_json())
        response.set_cookie(self.app.config['COOKIE_NAME'], base64.b16encode(chiphertext))

    def GetCookies(self, request):
        if request is not None:
            decrypted = request.cookies.get(self.app.config['COOKIE_NAME'])
            if decrypted is not None:
                cookies = base64.b16decode(decrypted)
                aes = pyaes.AESModeOfOperationCTR(self.app.config['SECRET_KEY'])
                decrpyted = aes.decrypt(cookies)
                return decrpyted
            else:
                return None
        else:
            return None

    # 쿠키 내역 아이디만 추출
    def GetUserID(self, request):
        c = self.GetCookies(request)
        user = UserVO()
        if c is not None:
            user.to_object(c)
        return user.user_id

    # 쿠키 체크 decorator
    def CheckCookie(self, f):
        @wraps(f)
        def _check_cookie_(*arg, **kwargs):
            cookie = self.GetCookies(request)
            if cookie is None:
                return redirect('/')
            return f(*arg, **kwargs)

        return _check_cookie_

    #로그인 체크
    def IsLogin(self, request):
        if self.GetUserID(request) is None:
            return False
        return True