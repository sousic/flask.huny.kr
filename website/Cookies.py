# -*- coding: UTF-8 -*-
from .utils import encode_cooie, decode_cookie

# try:
#     from http.cookiejar import CookieJar
# except ImportError: #P2
#     from cookielib import CookieJar

class Cookies(object):

    def __init__(self, app = None, add_context_proecessor=True):
        if app is not None:
            self.init_app(app, add_context_proecessor)

    #flask 쿠키 생성 객체 초기화
    def init_app(self, app, add_context_proecessor=True):

        if add_context_proecessor:
            app.context_processor(_user_context_processor)

    def setCookie(self, cookieName, data):
        pass

    def getCookie(self, cookieName):
        pass