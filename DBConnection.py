# coding=UTF-8
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

class DBCont(object):

    def __init__(self):
        self.getCon()

    # 获取连接
    def getCon(self):
        try:
            self.conn = MySQLdb.connect(
                host="127.0.0.1",
                user="root",
                passwd="root",
                db="monitor",
                port=3306,
                charset="utf8"
            )
            print ("数据库已连接")
        except MySQLdb.Error as e:
            print ("Error is %s,数据库连接出错啦！！！" % e)

    # 关闭连接
    def closeCon(self):
        try:
            if self.conn:
                self.conn.close()
                print ("数据库已关闭")
        except MySQLdb.error as e:
            print ("Error is %s,数据库关闭错误！！！" % e)

    def findOne(self):
        sql = "select * from authority Limit 1"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        print (rest)
        cursor.close()
        self.closeCon()



