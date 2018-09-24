#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/22 22:46
# @Author : leifengchuan
# @File : myUtilFile

"""
封装些常用的代码方法
比如包含发送邮件的方法
"""
#导入包
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pymysql# pip install pymysql
import time as time


# 第三方 SMTP 服务，采用网易邮箱的服务
mail_host = "smtp.XXX.com"  # 设置服务器
mail_user = "XXXX"  # 用户名
mail_pass = "XXXXXX"  # 口令
sender = 'from@runoob.com'
receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 定义数据库账号密码等信息
host = "localhost"
userName = "root"
password = "root"
mysqldbName = "stockAI"


def getCurrentFormateTime():
    """
    格式化日期:格式化成2016-03-20 11:45:39形式
    :return:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def getReceiversFromMysql():
    """
    从mysql数据库获取收件人列表
    :return:
    """
    sql="select email from reemail where status='1' "
   # return contnectMysqlDbAndFetchAll(sql)


def sedEmail(content,header):
    """
    定义发送邮件的方法
    :return:
    content:待发送的文本的内容
    header:头部信息

    """
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(header, 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



def createOrWriteContentToFile(string):
    """
    string：等待写入的日志信息
    :param string:
    :return:
    """
    string=string+"\n"#换行,追加模式
    with open("../../doc/stockAI.log",'a',encoding='UTF-8') as file:
        file.write(string)





def connectDB():
    """
    链接数据库返回db对象
    :return:
    """
    return pymysql.connect(host, userName, password, mysqldbName)


def contnectMysqlDbAndFetchOne(sql):
    """
    定义一个方法
    连接数据库，执行sql语句
    查询使用一条数据
    """
    # 打开数据库连接
    db = connectDB()

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    # 关闭数据库连接
    db.close()
    string="调用查询数据库的语句是{},查询时间:{}".format(sql,getCurrentFormateTime())
    createOrWriteContentToFile(string)
    return data


def contnectMysqlDbAndFetchAll(sql):
    """
    定义一个方法
    连接数据库，执行sql语句
    查询使用全部
    """
    # 打开数据库连接
    db = connectDB()

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    string = "调用查询数据库的语句是{},查询时间:{}".format(sql,getCurrentFormateTime())
    createOrWriteContentToFile(string)
    return data


def contnectMysqlDbAndFetchMany(sql):
    """
    定义一个方法
    连接数据库，执行sql语句
    查询使用多条数据
    """
    # 打开数据库连接
    db = connectDB()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchmany()
    # 关闭数据库连接
    db.close()
    string="调用查询数据库的语句是{},查询时间:{}".format(sql,getCurrentFormateTime())
    createOrWriteContentToFile(string)
    return data


def insterOrUpdateOrDelete(sql):
    """
    定义一个方法
    连接数据库，执行sql语句
    插入，更新，删除
    """
    # 打开数据库连接
    db = connectDB()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    string = "调用数据库的语句是{},查询时间:{}".format(sql, getCurrentFormateTime())
    createOrWriteContentToFile(string)
    db.close()




if __name__ == "__main__":
    sql = "select email from reemail where status='1' "
    print(contnectMysqlDbAndFetchAll(sql))


