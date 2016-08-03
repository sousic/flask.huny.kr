# -*- coding: UTF-8 -*-
from flask import Flask

app = Flask(__name__)
app.config.from_object('websiteconfig')

from views.home import home
app.register_blueprint(home.mod)