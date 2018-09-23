#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2018/9/22 22:46
# @Author : leifengchuan
# @File : mysqlUtil
"""
封装些常用的代码方法
比如包含链接mysql数据的方法
"""
# pip install pymysql
import pymysql


#定义账号密码等信息
host="localhost"
userName="root"
password="root"
mysqldbName="stockAI"


def connectDB():
    """
    链接数据库返回db对象
    :return:
    """
    return pymysql.connect(host,userName,password,mysqldbName)




def contectMysqlDbAndFetchOne(sql):
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
    # 执行sql语句
    db.commit()
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    # 关闭数据库连接
    db.close()
    return data


def contectMysqlDbAndFetchAll(sql):
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
    # 执行sql语句
    db.commit()
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return data


def contectMysqlDbAndFetchMany(sql):
    """
    定义一个方法
    连接数据库，执行sql语句
    查询使用多条数据
    """
    # 打开数据库连接
    db =connectDB()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchmany()
    # 关闭数据库连接
    db.close()
    return data



def insterOrUpdateOrDelete(sql):
    """
    定义一个方法
    连接数据库，执行sql语句
    插入，更新，删除
    """
    # 打开数据库连接
    db =connectDB()
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
    db.close()
    return data






if __name__=="__main__":
    sql="SELECT VERSION()"
    data=contectMysqlDbAndFetchOne(sql)
    print ("Database version : %s " % data)


    
