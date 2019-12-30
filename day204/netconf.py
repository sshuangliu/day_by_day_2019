#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/24 11:21
#@Author: max liu
#@File  : netconf.py

# centos7 安装yang-explorer（基于python2）:
"""

1：pip2 install --upgrade pip
2：yum install -y git
3:pip2 install virtualenv pyang
4:git clone https://github.com/CiscoDevNet/yang-explorer.git
5:cd yang-explorer 替换'setup.sh'中pip为pip2（我当前环境下pip -V 为pip3）
6：bash setup.sh
7：cd v/bin/ （进入virtualenv环境目录下）
8：./pip2 install graphviz jinja2 requests
9：cd yang-explorer/server/static
10: vi server/static/YangExplorer.html
    前端 服务器ip 端口号
    flashvars.host = '192.168.59.37';
    flashvars.port = 8088;
11：vi start.sh 后端服务器ip 端口号
    HOST='192.168.59.37'
    PORT='8088'
12：./start.sh
13：guest/guest


Activate Virtualenv
$ cd /yang-explorer
$ source v/bin/activate

Deactivate virtualenv
$ deactivate
"""
if __name__ == '__main__':
    pass