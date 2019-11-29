# coding=utf-8
import sys
import MySQLdb


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    # 检查账户是否合法
    def check_acct_avaiable(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from user where id=%s" % acctid
            cursor.execute(sql)
            print("check account:" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("user %s illega" % acctid)
        finally:
            cursor.close()

    # 检查是否有足够的钱
    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from user where id=%s and money > %s" % (acctid, money)
            cursor.execute(sql)
            print("has enough money:" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("user %s not enough money" % acctid)
        finally:
            cursor.close()

    # 账户减钱
    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update user set money = money-%s where id = %s" % (money, acctid)
            cursor.execute(sql)
            print("reduce_money:" + sql)
            if cursor.rowcount != 1:
                raise Exception("reduce money fail %s" % acctid)
        finally:
            cursor.close()

    # 账户加钱
    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update user set money = money+%s where id = %s" % (money, acctid)
            cursor.execute(sql)
            print("add_money:" + sql)
            if cursor.rowcount != 1:
                raise Exception("add money fail %s" % acctid)
        finally:
            cursor.close()

    # 主执行语句
    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_avaiable(source_acctid)
            self.check_acct_avaiable(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


if __name__ == "__main__":
    print(sys.argv)
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user='root', passwd='159357', db='test', charset='utf8')
    tr_money = TransferMoney(conn)
    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print("Happen:" + str(e))
    finally:
        conn.close()
