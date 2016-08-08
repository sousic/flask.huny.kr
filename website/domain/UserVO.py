# -*- coding: UTF-8 -*-
from datetime import datetime

from flask import json


class UserVO():

    seq = 0
    id = ''
    password = ''
    date = datetime.now()

    def to_json(self):
        return json.dumps(self.__dict__)
