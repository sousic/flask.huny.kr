# -*- coding: UTF-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for

from website.domain.UserVO import UserVO

class member():
    mod = Blueprint('member', __name__, url_prefix='/member')

    @mod.route('/regist/', methods=['GET','POST'])
    def regist():
        if request.method == 'POST':
            user = UserVO()
            user.id = request.form['userid']
            user.password = request.form['userpwd']
            user.user_name = request.form['username']

            return redirect(url_for('home.main'))

        return render_template('member/regist.html', title='Register', nav_title='Register')