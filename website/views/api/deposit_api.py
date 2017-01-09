# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify
from flask import request

from website import common_dao, cookie_helper
from website.domain import basicVO
from website.domain.api.jsonBasicVO import jsonBasic
from website.persistence.depositDAO import depositDAO

deposit_dao = depositDAO(common_dao)


class deposit_api():
    mod = Blueprint('api_deposit', __name__, url_prefix='/api/deposit')

    @mod.route("/list")
    def list():
        if cookie_helper.IsLogin(request) is True:
            result = jsonBasic(1, "OK", deposit_dao.selectDeposit(year=2016, month=None, user_id=None))

            return result.to_jsoin()
            #return deposit_dao.selectDeposit(year=2016, month=None, user_id=None)
        else:
            return jsonify(basicVO)