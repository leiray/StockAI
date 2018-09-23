#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/22 22:35
# @Author : leifengchuan
# @File : StockAI.py
"""
对外提供接口服务的文件


"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
