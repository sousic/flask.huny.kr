# -*- coding: UTF-8 -*-
import flask_login
from flask import Flask, Blueprint, render_template, redirect, url_for, request
from website import User


class home:
    mod = Blueprint('home', __name__)

    @mod.route('/')
    def home():
        return render_template('home/index.html', title = 'Home')

    @mod.route('/login/')
    def login():
        #if request.method == 'GET':
        user = User()
        user.id = 'test'
        user.state = 'admin'

        flask_login.login_user(user)
        return ''
        #return redirect(url_for('/'))

    @mod.route("/check/")
    @flask_login.login_required
    def login_check():
        print flask_login._get_user().id, flask_login._get_user().state
        return ''