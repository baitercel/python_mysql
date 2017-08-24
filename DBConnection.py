# coding=UTF-8
import MySQLdb

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
                db="news",
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

    # 取出单个值
    def findOne(self):
        sql = "select * from news Limit 1"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        print (rest)
        cursor.close()
        self.closeCon()

    # 取出多个值
    def findMore(self):
        sql = "select * from news authority"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = [dict(zip([k[0] for k in cursor.description], row))for row in cursor.fetchall()]
        for i in rest:
            print (i)
            print ("------")
        cursor.close()
        self.closeCon()

    # 添加一个值
    def addOne(self):
        try:
            sql = "INSERT INTO news(title,image, content, types) VALUES(%s,%s,%s,%s);"
            cursor = self.conn.cursor()
            cursor.execute(sql, ("aa", "bb", "cc", "dd"))
            self.conn.commit()
            cursor.close()
            print ("插入数据成功")
        except Exception as e:
            print (e+"插入数据库异常")
            self.conn.rollback()
        self.closeCon()

