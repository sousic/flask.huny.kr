# -*- coding: UTF-8 -*-
from flask import Flask

from website import CustomFilters
from website.CookieHelper import CookieHelper
from website.persistence.commonDAO import commonDAO

app = Flask(__name__)
#필터 등록
app.jinja_env.filters['number_format'] = CustomFilters.filter_number_format

app.config.from_object('websiteconfig')

cookie_helper = CookieHelper()
cookie_helper.init_app(app)

common_dao = commonDAO(app)

from views.home import home
from views.member import member
from views.deposit import deposit

app.register_blueprint(home.mod)
app.register_blueprint(member.mod)
app.register_blueprint(deposit.mod)