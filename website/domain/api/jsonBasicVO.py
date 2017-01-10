# -*- coding: UTF-8 -*-
from flask import jsonify

class jsonBasic():
    resultCode = 0
    resultMsg = None
    result = None

    def __init__(self, resultCode, resultMsg, result=None):
        self.resultCode = resultCode
        self.resultMsg = resultMsg
        self.result = result

    def to_jsoin(self):
        return jsonify(self.__dict__)
