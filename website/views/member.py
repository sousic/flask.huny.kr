# -*- coding: UTF-8 -*-
from unittest import result

import bcrypt
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from website import common_dao
from website.domain.UserVO import UserVO
from website.persistence.memberDAO import memberDAO
from website.utils import *


class member():
    mod = Blueprint('member', __name__, url_prefix='/member')

    @mod.route('/regist', methods=['GET','POST'])
    def regist():
        if request.method == 'POST':
            user = UserVO()
            user.user_id = request.form['userid']
            user.user_pwd = bcrypt.hashpw(request.form['userpwd'].encode('utf8'), bcrypt.gensalt())
            user.user_name = request.form['username']

            member_dao = memberDAO(common_dao)
            user_id = member_dao.memberIdCheck(user)
            print type(user_id)
            if len(user_id) == 0:
                member_dao.memberInsert(user)

                setMessage(1, 'OK')
                return jsonify(jsonResult)
            else:
                setMessage(-1, u'아이디 중복')
                return jsonify(jsonResult)

            setMessage(-1, u'필수 항목 누락')
            return jsonify(jsonResult)

        return render_template('member/regist.html', title='Register', nav_title='Register')

    @mod.route('/idcheck', methods=['POST'])
    def idcheck():
        if request.method == 'POST':
            user = UserVO()
            user.user_id = request.form['userid']

            member_dao = memberDAO(common_dao)
            user_id = member_dao.memberIdCheck(user)

            if len(user_id) == 1:
                setMessage(-1, u'아이디 중복')
                return jsonify(jsonResult)
            else:
                setMessage(1, 'OK')
                return jsonify(jsonResult)

        setMessage(-1, u'필수 항목 누락')
        return jsonify(jsonResult)