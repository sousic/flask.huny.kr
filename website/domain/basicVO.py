# -*- coding: UTF-8 -*-
from flask import json

#JSON 파싱 지원을 위한 최상위 클래스
class basicVO():
    def to_json(self):
        return json.dumps(self.__dict__)

    def to_object(self, j):
        self.__dict__ = json.loads(j)