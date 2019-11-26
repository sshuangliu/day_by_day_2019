#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/11/26 14:04
#@Author: max liu
#@File  : matplotlib_cpu_usage.py

from matplotlib import pyplot as plt
import matplotlib
import random
import time
from datetime import datetime, timedelta

plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文
plt.rcParams['font.family'] = 'sans-serif'


def randomtimes(start, end=None, n=1, frmt="%H:%M:%S"):
    stime = datetime.strptime(start, frmt)
    # etime = datetime.datetime.strptime(end, frmt)
    # print(stime)
    return stime+timedelta(seconds=10*n)


usage_dict_temp = {}
for i in range(10):
    usage_dict_temp[randomtimes('08:30:00', n=i)] = {'cpu_usage': '%.1f' % (random.random() * 100), 'memory_usage': '%.1f' % (random.random() * 100)}
# print(usage_dict_temp)


def mat_line(usage_dict):
    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行, 每行一图, 第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate
    ax.xaxis.set_major_formatter(mdate.DateFormatter("%H:%M:%S")) # 设置时间标签显示格式 该格式需要和时间数据类型及格式一致
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f%%')) #  Y轴百分比格式，Y轴数据需要float类型 才能匹配

    # 把usage_dict的数据,拆分为x轴的时间,与y轴的利用率
    x = [x for x in usage_dict.keys()]
    y1 = [float(y1['cpu_usage']) for y1 in list(usage_dict.values())]
    y2 = [float(y2['memory_usage']) for y2 in list(usage_dict.values())]
    print(x)
    print(y1)
    print(y2)

    # 添加主题和注释
    plt.title('路由器CPU利用率')
    plt.xlabel('采集时间')
    plt.ylabel('设备CPU\Memory利用率')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应

    # 实线红色
    ax.plot(x, y1, linestyle='solid', color='red', label='CPU')
    # 虚线黑色
    ax.plot(x, y2, linestyle='dashed', color='blue', label='Memory')


    # 设置说明的位置
    ax.legend(loc='upper right')

    # 保存到图片
    # plt.savefig('device_usage.png')
    for time_, cpu_percent in zip(x, y1):
        plt.text(time_, cpu_percent + 0.1, cpu_percent, verticalalignment="bottom", horizontalalignment="center")

    for time_, memory_percent in zip(x, y2):
        plt.text(time_, memory_percent+0.1, memory_percent, verticalalignment="top", horizontalalignment="center")

    # 绘制图形
    plt.show()

if __name__ == '__main__':
    mat_line(usage_dict_temp)