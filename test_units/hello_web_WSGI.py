#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/30 11:13
# @Author: max liu
# @File  : hello_web_WSGI.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ)
    print(start_response)
    return [b'<h1>Hello, web!</h1>']
