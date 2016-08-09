# -*- coding: UTF-8 -*-
from flask import jsonify

jsonResult = dict(result=0, msg='')

def setMessage(result, msg):
    jsonResult['result'] = result
    jsonResult['msg'] = msg