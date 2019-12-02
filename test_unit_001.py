#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/10/26 22:07
# @Author: max liu
# @File  : test_unit_001.py

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


# #运行一个简单的HTTP服务器
# from http.server import HTTPServer, CGIHTTPRequestHandler
#
# port = 80
# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
# print('Starting simple httpd on port: ' + str(httpd.server_port))
# httpd.serve_forever()


# import ifaddr as ifaddr
import datetime as datetime
from kamene.all import *
import logging

#
# logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
# # from kamene.layers.inet import IP, ICMP
#
# ping_pkt = IP(dst='1.1.1.1') / ICMP(type=8, code=0)  # 制造一个Ping包
# ping_result = sr(ping_pkt, timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result
# print(ping_result)
#
#
# # show_interfaces()
# print(get_if_list())
#
# class Networkerror(Exception):
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __str__(self):
#         return repr(self.arg)
#
#
# try:
#     raise Networkerror("Bad hostname")
# except Networkerror as e:
#     print(type(e))
#     print(e)


# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(-101, 101, 1)
#
# plt.plot(x, x ** 2)
# # 查看此时的x轴的最大值和最小猪和y轴的最大值最小值
# # print plt.axis()
# # 设置四个最值，列表传入
# # plt.axis([-100, 100, 0, 10000])
#
# # 查看此时x轴的最大值和最小值
# print(plt.xlim())
# # 设置最大值和最小值(可以两个都设置，也可以只设置一个，只设置一个的时候要显式声明)
# # plt.xlim(-200, 200)
# # 显式指定
# # plt.xlim(xmin = -200, xmax = 200)
# # plt.xlim(xmin=-200)
# # plt.xlim(xmax=100)
# plt.ylim(ymin=0)
#
# # 还有专门针对于y轴而言的ylim，xlim具备的方法ylim都具备，不再描述
#
# plt.show()


# import matplotlib.pyplot as plt
# # import matplotlib
# #
# # matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# # matplotlib.rcParams['axes.unicode_minus'] = False
# #
# # price = [39.5, 39.9, 45.4, 38.9, 33.34]
# # """
# # 绘制水平条形图方法barh
# # 参数一：y轴
# # 参数二：x轴
# # """
# # plt.barh(range(5), price, height=0.7, color='steelblue', alpha=0.8)      # 从下往上画
# # plt.yticks(range(5), ['亚马逊', '当当网', '中国图书网', '京东', '天猫'])
# # plt.xlim(30,47)
# # plt.xlabel("价格")
# # plt.title("不同平台图书价格")
# # for x, y in enumerate(price):
# #     print(x)
# #     plt.text(y + 0.3, x - 0.1, '%s' % y)
# # plt.show()


# import matplotlib, random
#
# # hex_colors_dic = {}
# # rgb_colors_dic = {}
# # hex_colors_only = []
# # for name, hex in matplotlib.colors.cnames.items():
# #     hex_colors_only.append(hex)
# #     hex_colors_dic[name] = hex
# #     rgb_colors_dic[name] = matplotlib.colors.to_rgb(hex)
# #
# # print(hex_colors_only)
# # print(hex_colors_dic)
# # print(rgb_colors_dic)
# # print(hex_colors_dic['snow'])
# # # getting random color from list of hex colors
# #
# # print(random.choice(hex_colors_only))
# a = matplotlib.colors.cnames
# print(random.sample(list(a.keys()), 5))
# print(random.sample(list(a.values()), 5))


# !/usr/bin/python
# coding: utf-8

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 100)
#
# fig = plt.figure()
#
# ax1 = fig.add_subplot(221)
# ax1.plot(x, x)
#
# ax2 = fig.add_subplot(222)
# ax2.plot(x, -x)
#
# ax3 = fig.add_subplot(223)
# ax3.plot(x, x ** 2)
#
# ax4 = fig.add_subplot(224)
# ax4.plot(x, np.log(x))
#
# ax5 = fig.add_subplot(225)
# ax5.plot(2*x, np.log(x))
#
# plt.show()


# -*- coding: utf-8 -*-
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdate
# import pandas as pd
# from datetime import datetime
# import time
#
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#
#
#
# y1 = [0.9143, 0.9293, 0.9348, 0.9327]
# y2 = [0.9143, 0.9294, 0.9348, 0.9327]
#
# fig = plt.figure(figsize=(15, 10))
# ax = fig.add_subplot(1, 1, 1)
# ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y%m%d'))  # 设置时间标签显示格式
# ax.xaxis.set_major_locator(mdate.DayLocator())
# ax.set_title("y plot")
# ax.plot(date, y1, 'go-', label=u'这是y1')
# ax.plot(date, y2, 'yo-', label=u'这是y2')
# plt.xticks(rotation=45)  # 旋转45度显示
# legend = ax.legend(loc='lower center', shadow=False)
# plt.show()

from datetime import datetime

# import random
# import time
# date1 = {}
# for i in range(3):
#     date1[time.strftime('%Y%m%d-%H%M%S')] = '%.1f%%' % (random.random()*100)
#     time.sleep(1)
# print(date1)

# python2 不兼容，python3正常
# import datetime,random
# def randomtimes(start, end, n, frmt="%Y-%m-%d"):
#     stime = datetime.datetime.strptime(start, frmt)
#     etime = datetime.datetime.strptime(end, frmt)
#     print(stime)
#     print(etime)
#     return [random.random() * (etime - stime) + stime for _ in range(n)]
#
# print(randomtimes('2018-06-01','2018-11-01',2))


#
# usage_dict = {}
# for i in range(10):
#     usage_dict[time.strftime('%Y%m%d-%H%M%S')] = {'cpu_usage':'%.1f%%' % (random.random() * 100), 'memory_usage':'%.1f%%' % (random.random() * 100)}
#     time.sleep(2)
# print(usage_dict)
#
# x = [x for x in usage_dict.keys()]
# y1 = [y1['cpu_usage'] for y1 in list(usage_dict.values())]
# y2 = [y2['memory_usage'] for y2 in list(usage_dict.values())]
# print(x)
# print(y1)
# print(y2)


import time

# print ("time.time(): %f " %  time.time())
# print(type(time.time()))
# print (time.localtime( time.time() ))
# print(type(time.localtime(time.time())))
# print (time.asctime( time.localtime(time.time()) ))
# print(type(time.asctime( time.localtime(time.time()))))
#
# from datetime import datetime
# import os
# from apscheduler.schedulers.blocking import BlockingScheduler
#
#
# def tick():
#     print('Tick! The time is: %s' % datetime.now())
#
#
# if __name__ == '__main__':
#     scheduler = BlockingScheduler()
#     scheduler.add_job(tick, 'interval', seconds=3)
#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
#
#     try:
#         scheduler.start()
#     except (KeyboardInterrupt, SystemExit):
#         pass
#
#
# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
# import datetime
# import logging
#
# #  2019-11-28 15:44:11 base.py[line:440] INFO Adding job tentatively -- it will be properly scheduled when the scheduler starts
# logging.basicConfig(level=logging.INFO,
#                       format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                       datefmt='%Y-%m-%d %H:%M:%S',
#                       filename='apscheduler_log1.txt',
#                       filemode='a')
#
#
# def aps_test(x):
#       print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
#
#
# def date_test(x):
#       print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
#       print (1/0)
#
#
# def my_listener(event):
#       if event.exception:
#           print ('任务出错了！！！！！！')
#       else:
#           print ('任务照常运行...')
#
# scheduler = BlockingScheduler()
# scheduler.add_job(func=date_test, args=('一次性任务,会出错',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15), id='date_task')
# scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=3, id='interval_task')
# scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# scheduler._logger = logging
#
# scheduler.start()

from datetime import datetime
# import os
# from apscheduler.schedulers.blocking import BlockingScheduler
#
#
# class test:
#     def tick(self, a, b, c):
#         # print('Tick! The time is: %s' % datetime.now())
#         print(a)
#         print(b)
#         print(c)
#
#
# if __name__ == '__main__':
#     t = test()
#     scheduler = BlockingScheduler()
#     scheduler.add_job(t.tick, trigger='interval', args=('ha', 'haha', 'hahaha'), seconds=3)
#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
#
#     try:
#         scheduler.start()
#     except (KeyboardInterrupt, SystemExit):
#         pass

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'

x = np.linspace(-10, 10)
y = np.sin(x)

# 211表示，要绘制的图是2行1列，最后一个1，表示的是子图中的第一个图
plt.subplot(211)
plt.plot(x, y, color='r')
plt.title('路由器CPU利用率')
plt.xlabel('采集时间')
plt.ylabel('设备CPU\Memory利用率')

plt.subplot(212)
plt.plot(x, y, color='b')

# 添加主题和注释
plt.title('路由器CPU利用率')
plt.xlabel('采集时间')
plt.ylabel('设备CPU\Memory利用率')
plt.show()
