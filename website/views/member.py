# -*- coding: UTF-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from website import common_dao
from website.domain.UserVO import UserVO
from website.persistence.memberDAO import memberDAO


class member():
    mod = Blueprint('member', __name__, url_prefix='/member')

    @mod.route('/regist', methods=['GET','POST'])
    def regist():
        if request.method == 'POST':
            user = UserVO()
            user.id = request.form['userid']
            user.password = request.form['userpwd']
            user.user_name = request.form['username']

            member_dao = memberDAO(common_dao)
            user_id = member_dao.memberIdCheck(user)
            print 'user_id :', user_id

            return redirect(url_for('home.main'))

        return render_template('member/regist.html', title='Register', nav_title='Register')

    @mod.route('/idcheck', methods=['POST'])
    def idcheck():
        result = dict(result=0,msg='')
        if request.method == 'POST':
            user = UserVO()
            user.id = request.form['userid']

            member_dao = memberDAO(common_dao)
            user_id = member_dao.memberIdCheck(user)

            if user_id is None:
                result['result'] = -1
                return jsonify(result)
            else:
                result['result'] = 1
                return jsonify(dict(result=1))

        result['result'] = -1
        result['msg'] = 'Not UserID'

        return jsonify(result)