#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/15 16:33
# @Author: max liu
# @File  : json_rpc_requests.py

import requests
import base64

r = requests.post(url='http://192.168.59.37:7777/rest/time', json={'function': 'date'},
                  headers={'Content-Type': 'application/xml'})
print(r.request.headers)
print(r.headers)
print(r.json())
r = requests.post(url='http://192.168.59.37:7777/rest/time', json={'function': 'datetime'})
print(r.request.headers)
print(r.headers)
print(r.json())

r = requests.post(url='http://192.168.59.37:7777/rest/cmd', json={'cmd': 'ip add'})
print(r.request.headers)
print(r.headers)
print(r.json().get('result'))
a = base64.b64decode(r.json().get('result')).decode('utf-8')  # B64解码对象r,解码后为byte，需要decode为str
print(a)

date_path = r'C:\Users\liushuang\Desktop\syslog.rar'
with open(date_path, 'rb') as f:  # 不能open  read 一起??
    date = base64.b64encode(f.read()).decode('utf-8')
r = requests.put(url='http://192.168.59.37:7777/upload/syslog.rar', json={'file': date})
# print(r.json())
print(r.status_code)
print('puttttt')
r = requests.get(url='http://192.168.59.37:7777/download/MyLanViewerchs.zip')
with open('lanview.zip', 'wb') as f:
    f.write(base64.b64decode(r.json().get('result')))
# print(r.json())
print(r.status_code)
print('gettttt')