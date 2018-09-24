#!/usr/bin/python3
# -*- coding:utf-8 -*- 
'''
created by leifengchuan
'''
"""
pip install APScheduler
第三种方法实现定时器
https://blog.csdn.net/blueheart20/article/details/70219490?locationNum=1&fps=1
https://segmentfault.com/a/1190000011084828
https://segmentfault.com
https://www.cnblogs.com/hushaojun/p/5189109.html
【最好的模式】
"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime




def job_function():
    """
    定义一个定时器的方法
    用来执行具体的细节功能
    :return:
    """
    print("Hello World "  + str(datetime.datetime.now()))
    "Hello World" + " " + str(datetime.datetime.now())





if __name__ == '__main__':
    """
    代码执行测试
    """
    print('start to do it')
    sched = BlockingScheduler()
    sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour='0-23', minute="*", second="*/1")
    sched.start()