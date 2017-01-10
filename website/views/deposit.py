# -*- coding: UTF-8 -*-
from flask import Blueprint
from flask import render_template

from website import common_dao, cookie_helper
from website.persistence.depositDAO import depositDAO
from website.views import naviHelper

deposit_dao = depositDAO(common_dao)

class deposit():
    mod = Blueprint('deposit', __name__, url_prefix='/deposit')

    @mod.route('/')
    @cookie_helper.CheckCookie
    def index():
        tabNaviList = naviHelper.printNavi()

        return render_template('deposit/index.html', tabNaviList = tabNaviList)
        #, **locals())
