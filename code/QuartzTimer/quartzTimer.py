#!/usr/bin/python3
# -*- coding:utf-8 -*- 
'''
created by leifengchuan
'''
from threading import Timer



def printHello():
    """
    定时器模式一：
    直接使用thrading中的timer
    :return:
    """
    print("Hello World")
    "Hello World"
    t = Timer(10*2, printHello)
    t.start()


if __name__ == "__main__":
    printHello()

