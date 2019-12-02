#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/11/30 11:14
#@Author: max liu
#@File  : WSGU_server.py


# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from test_units.hello_web_WSGI import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('192.168.157.37', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()





if __name__ == '__main__':
    pass