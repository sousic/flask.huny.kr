# -*- coding: UTF-8 -*-
from flask import Flask

from website.CookieHelper import CookieHelper

app = Flask(__name__)
app.config.from_object('websiteconfig')

cookie_helper = CookieHelper()
cookie_helper.init_app(app)

from views.home import home
app.register_blueprint(home.mod)
