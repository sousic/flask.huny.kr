# -*- coding: UTF-8 -*-
import datetime
from website.domain.basicVO import basicVO


class depositVO(basicVO):
    seq = 0
    month = datetime.date.year
    month = datetime.date.day
    user_id = ''
    amount = 0
    reg_date = datetime.now()