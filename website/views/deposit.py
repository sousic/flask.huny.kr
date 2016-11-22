# -*- coding: UTF-8 -*-
from flask import Blueprint
from flask import render_template

from website import common_dao
from website.persistence.depositDAO import depositDAO
from website.views import naviHelper

deposit_dao = depositDAO(common_dao)

class deposit():
    mod = Blueprint('deposit', __name__, url_prefix='/deposit')

    @mod.route('/')
    def index():
        nav_title = naviHelper.printNavi()

        result = deposit_dao.selectDeposit(year=2016, month=None, user_id=None)
        return render_template('deposit/index.html', **locals())
