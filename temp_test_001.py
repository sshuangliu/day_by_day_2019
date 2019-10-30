#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/10/26 22:07
#@Author: max liu
#@File  : temp_test_001.py

# import re
# import os
# #a = os.popen('ip add').read()
# #print(a)
#
#
# #os.chdir('day007/test')
# print(os.getcwd())
#
# #port_infor = os.popen('netstat -ano|findstr "80"').read().split('\n')
# port_infor = os.popen('netstat -ltnp').read().split('\n')
#
# for i in port_infor:
#
#     print(i)
#
# # 测试
#
# print(re.findall(r'/bbc/b', 'eeegfd bc dad'))


#运行一个简单的HTTP服务器
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 80
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()