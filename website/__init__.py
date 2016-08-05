# -*- coding: UTF-8 -*-
from flask import Flask
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config.from_object('websiteconfig')

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    pass

users = { 'test' : {'pw' : 'test'}}


@login_manager.user_loader
def user_loader(id):
    if id not in users:
        return

    user = User()
    user.id = id
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['id'] == users[id]

    return user

from views.home import home
app.register_blueprint(home.mod)