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

# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
# plt.rcParams['font.family'] = 'sans-serif'
#
# x = np.linspace(-10, 10)
# y = np.sin(x)
#
# # 211表示，要绘制的图是2行1列，最后一个1，表示的是子图中的第一个图
# plt.subplot(211)
# plt.plot(x, y, color='r')
# plt.title('路由器CPU利用率')
# plt.xlabel('采集时间')
# plt.ylabel('设备CPU\Memory利用率')
#
# plt.subplot(212)
# plt.plot(x, y, color='b')
#
# # 添加主题和注释
# plt.title('路由器CPU利用率')
# plt.xlabel('采集时间')
# plt.ylabel('设备CPU\Memory利用率')
# plt.show()


# # In Python 3.2+:
#
# >>> bin(int.from_bytes('hello'.encode(), 'big'))
# '0b110100001100101011011000110110001101111'
# # In reverse:
#
# >>> n = int('0b110100001100101011011000110110001101111', 2)
# >>> n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
# # 'hello
#
# import tkinter
# import tkinter.messagebox
#
#
# def main():
#     flag = True
#
#     # 修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ('red', 'Hello, world!')\
#             if flag else ('blue', 'Goodbye, world!')
#         label.config(text=msg, fg=color)
#
#     # 确认退出
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
#             top.quit()
#
#     # 创建顶层窗口
#     top = tkinter.Tk()
#     # 设置窗口大小
#     top.geometry('240x160')
#     # 设置窗口标题
#     top.title('小游戏')
#     # 创建标签对象并添加到顶层窗口
#     label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
#     label.pack(expand=1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
#     button1 = tkinter.Button(panel, text='修改', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()


# # 文件内容替换
# import os
# import re
#
# # 遍历方式为以文件夹为主线遍历 root:当前遍历的文件夹绝对路径，dirs:当前遍历路径下文件夹的列表 files：当前遍历路径下文件的列表
# for root, dirs, files in os.walk("D:\T1", topdown=True):
#     for item in dirs:
#         for root1, dirs1, files1 in os.walk(os.path.join(root, item), topdown=True):
#             for i in files1:
#                 if '.vmx' == os.path.splitext(i)[1]:
#                     with open(os.path.join(root1, i), 'r+') as f: # + 以seek（teel）位置逐行覆盖写; w/w+:先清空，慎用
#                         if re.findall(r'vmci0.present = "True"', f.read(10240)):
#                             f.seek(0)
#                             new_data = re.sub(r'vmci0.present = "True"', 'vmci0.present = "false"', f.read(10240),
#                                               count=1)
#                             f.seek(0)
#                             f.write(new_data)
#                             print('已修改:', os.path.join(root1, i))
#                         else:
#                             print('无需修改:', os.path.join(root1, i))
#                     break
#             break
#     break


# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
# plt.rcParams['font.family'] = 'sans-serif'
#
# labels = ['python基础', 'python网络编程tcp/ip', 'http协议', 'Django', 'Ansible/Zabbix/ELK', '网络自动化运维项目开发实践','总课时']
# men_means = [18, 21, 9, 12, 6, 9, 75]
# women_means = [16.8, 14.8, 10.2, 9.2, 4.3, 0, 55.3]
#
# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars
#
# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, men_means, width, label='官网宣传课时')
# rects2 = ax.bar(x + width/2, women_means, width, label='实际课时')
#
# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('课时(H)')
# ax.set_title('课时对比')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()
#
#
# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
#
#
# autolabel(rects1)
# autolabel(rects2)
# # fig.tight_layout()
# fig.autofmt_xdate()
#
# plt.savefig('class_time.png')
# plt.show()


# import multiprocessing
# import time
#
#
# def process(index):
#     print(f'process {index}')
#     time.sleep(index)
#
#
# for i in range(5):  # 非常规意义的按序的for循环，只是用于分配 创建进程的数量，
#     p = multiprocessing.Process(target=process, args=[i])
#     p.start()
#     print(f'haha {i}')
# print(f'cpu number {multiprocessing.cpu_count()}')
# for p in multiprocessing.active_children():
#     print(f'chile process name : {p.name} id : {p.pid}')
# print('process ended')

# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import jieba
#
# filename = "COVER-1.TXT"
# with open(filename) as f:
#     mytext = f.read()
#
# mytext = " ".join(jieba.cut(mytext))
# wordcloud = WordCloud().generate(mytext)
#
#
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
