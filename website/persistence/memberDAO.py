# -*- coding: UTF-8 -*-
from website.persistence.commonDAO import commonDAO


class memberDAO:
    def __init__(self, common_dao):
        self.common_dao = common_dao

    def memberInsert(self, user):
        pass

    def memberIdCheck(self, user):
        user_id = self.common_dao.executeQuery('select user_id from member where user_id = ?', [user.user_id])
        return user_id
