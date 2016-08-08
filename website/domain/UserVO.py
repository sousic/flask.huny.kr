# -*- coding: UTF-8 -*-
from datetime import datetime
from website.domain.basicVO import basicVO

class UserVO(basicVO):
    seq = 0
    id = ''
    password = ''
    date = datetime.now()