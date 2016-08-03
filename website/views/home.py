# -*- coding: UTF-8 -*-
from flask import Flask, Blueprint, render_template, redirect, url_for, request

class home:
    mod = Blueprint('home', __name__)

    @mod.route('/')
    def home():
        return render_template('home/index.html', title = 'Home')

    @mod.route('/login/', methods = ['POST','GET'])
    def login():
        if request.METHOD == 'GET':
            return redirect(url_for('/'))