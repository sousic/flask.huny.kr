# -*- coding: UTF-8 -*-
from flask import Flask

from website.CookieHelper import CookieHelper
from website.persistence.commonDAO import commonDAO

app = Flask(__name__)
app.config.from_object('websiteconfig')

cookie_helper = CookieHelper()
cookie_helper.init_app(app)

common_dao = commonDAO(app)

from views.home import home
from views.member import member
app.register_blueprint(home.mod)
app.register_blueprint(member.mod)
