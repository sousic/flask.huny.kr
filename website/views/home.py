# -*- coding: UTF-8 -*-
import base64

import pyaes
from flask import Flask, Blueprint, render_template, redirect, url_for, request
from flask import json
from flask import make_response

from website import cookie_helper
from website.domain.UserVO import UserVO

class home():
    mod = Blueprint('home', __name__)

    @mod.route('/')
    def index():
        return render_template('home/index.html', title = 'Index')

    @mod.route('/login/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            id = request.form['userid']
            password = request.form['userpwd']

            user = UserVO()
            user.seq = 0
            user.id = id
            user.password = password

            response = make_response(redirect(url_for('home.main')))
            cookie_helper.SetCookies(response, user)

            return response

        return redirect(url_for('home/main.html'))

    @mod.route('/main/')
    @cookie_helper.CheckCookie
    def main():
        #id = cookie_helper.GetUserID(request).id
        return render_template('home/main.html', title = '', userid = None)

    @mod.route('/register/')
    def register():
        return render_template('home/register.html', title = '')