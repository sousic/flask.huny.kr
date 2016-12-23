# -*- coding: UTF-8 -*-
from flask import request


class NaviInfo:
    def __init__(self, title, activeCSS, url_path, request_path):
        self.title = title
        self.activeCss = activeCSS
        self.url_path = url_path #링크 주소
        self.request_path = request_path

    def active(self):
        if self.request_path.startswith(self.url_path) is True:
            return self.activeCss;


def printNavi():
    currentUrlPath = request.path
    activeCSS = "class=\"active\""
    tab1 = NaviInfo(u"회원목록", activeCSS, '/member', currentUrlPath)
    tab2 = NaviInfo(u"이체내역", activeCSS, '/deposit', currentUrlPath)

    tabNaviList = [tab1, tab2]

    return tabNaviList


