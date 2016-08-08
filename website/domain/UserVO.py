# -*- coding: UTF-8 -*-
from datetime import datetime
from website.domain.basicVO import basicVO

class UserVO(basicVO):
    seq = 0
    id = ''
    password = ''
    pwd_fail_cnt = 0
    user_name = ''
    is_del = 0
    is_confirm = 0
    is_login_lock = 0
    date = datetime.now()