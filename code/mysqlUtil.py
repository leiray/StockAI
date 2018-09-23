#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2018/9/22 22:46
# @Author : leifengchuan
# @File : mysqlUtil

"""
封装些常用的代码方法
比如包含发送邮件的方法
"""

import pymysql
 




def contectMysqlDbAndFetchOne(sql):
    """
    定义一个方法
    连接数据库，执行sql语句
    """
   # 打开数据库连接
    db = pymysql.connect("localhost","root","root","stockAI" )
 
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
 
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    # 关闭数据库连接
    db.close()
    return data











if __name__=="__main__":
    sql="SELECT VERSION()"
    data=contectMysqlDB(sql)
    print ("Database version : %s " % data)


    
