# -*- coding: UTF-8 -*-

class depositDAO:
    def __init__(self, common_dao):
        self.common_dao = common_dao

    def insertDeposit(self, deposit):
        self.common_dao.insertQuery(
            'insert into deposit("year", "month", user_id, amount, reg_date) values(?, ?, ?, ?, ?)',
            [deposit.year, deposit.month, deposit.user_id, deposit.amount, deposit.reg_date])

    def selectDeposit(self, year, month, user_id):
        if year is not None:
            return self.common_dao.executeQuery('select * from deposit where year = ?', [year])
        elif year is not None and month is not None:
            return self.common_dao.executeQuery('select * from deposit where year = ? and month =?', [year, month])
        elif user_id is not None:
            return self.common_dao.executeQuery('select * from deposit where user_id = ? ', [user_id])
        else:
            return self.common_dao.executeQuery('select * from deposit')