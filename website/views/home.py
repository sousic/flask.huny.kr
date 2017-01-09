# -*- coding: UTF-8 -*-

from flask import Blueprint, render_template, redirect, url_for, request
from flask import make_response

from website import cookie_helper
from website.domain.UserVO import UserVO
from website.views import naviHelper


class home():
    mod = Blueprint('home', __name__)

    @mod.route('/')
    def index():
        return render_template('home/index.html', title='Index')

    @mod.route('/login/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user_id = request.form['userid']
            user_pwd = request.form['userpwd']

            user = UserVO()
            user.seq = 0
            user.user_id = user_id
            user.user_pwd = user_pwd

            response = make_response(redirect(url_for('home.main')))
            cookie_helper.SetCookies(response, user)

            return response

        return redirect(url_for('home/main.html'))

    @mod.route('/main/')
    @cookie_helper.CheckCookie
    def main():
        tabNaviList = naviHelper.printNavi()
        return render_template('home/main.html', title='', userid=cookie_helper.GetUserID(request), tabNaviList=tabNaviList)

    @mod.route('/register/')
    def register():
        return render_template('home/register.html', title='')
