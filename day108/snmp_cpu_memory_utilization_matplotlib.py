#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/1 15:16
# @Author: max liu
# @File  : snmp_cpu_memory_utilization_matplotlib.py


import pg8000
from matplotlib import pyplot as plt
import matplotlib
from datetime import datetime, timedelta

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'


def select_tab(stime):
    conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                          database='shuangdb_001')
    c = conn.cursor()

    #  查询表 列名又不需要''
    sql = f'''SELECT tdate, cpu_utilization,memory_utilization FROM device_cpu_memory_utilization where tdate >= '{datetime.strptime(stime, "%Y-%m-%d %H:%M:%S")}' and tdate < '{datetime.strptime(stime, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=1)}' '''  # 列名又不需要'' 艹！！！！
    results = c.execute(sql)
    results_all = results.fetchall()
    return results_all
    conn.commit()
    c.close()
    conn.close()


def snmp_matplotlib_line(stime):
    # cpu_utilization
    device_infor = select_tab(stime)
    x_date = [x[0] for x in device_infor]
    y1_cpu_utilization = [y1[1] for y1 in device_infor]
    y2_memory_utilization = [y2[2] for y2 in device_infor]
    print(x_date)
    print(y1_cpu_utilization)
    print(y2_memory_utilization)

    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))

    # 一共一行, 每行一图, 第一图
    ax1 = fig.add_subplot(211)
    # 添加主题和注释
    plt.title('cpu_utilization')
    plt.xlabel('time')
    plt.ylabel('percent')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应,斜着表示
    for time_, cpu_percent in zip(x_date, y1_cpu_utilization):
        plt.text(time_, cpu_percent + 0.1, cpu_percent, verticalalignment="bottom", horizontalalignment="center")

    ax2 = fig.add_subplot(212)
    # 添加主题和注释
    plt.title('memory_utilization')
    plt.xlabel('time')
    plt.ylabel('percent')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应,斜着表示

    for time_, memory_percent in zip(x_date, y2_memory_utilization):
        plt.text(time_, memory_percent + 0.1, memory_percent, verticalalignment="top", horizontalalignment="center")

    # 处理X轴时间格式
    import matplotlib.dates as mdate
    ax1.xaxis.set_major_formatter(mdate.DateFormatter("%H:%M:%S"))  # 设置时间标签显示格式 该格式需要和时间数据类型及格式一致
    ax2.xaxis.set_major_formatter(mdate.DateFormatter("%H:%M:%S"))  # 设置时间标签显示格式 该格式需要和时间数据类型及格式一致
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))  # Y轴百分比格式，Y轴数据需要int类型 与原始数据才能匹配
    ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))  # Y轴百分比格式，Y轴数据需要int类型 与原始数据才能匹配

    # 实线红色
    ax1.plot(x_date, y1_cpu_utilization, linestyle='solid', color='red', label='CPU')
    # 虚线黑色
    ax2.plot(x_date, y2_memory_utilization, linestyle='dashed', color='blue', label='Memory')

    # 设置说明的位置
    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')

    # 保存到图片
    # plt.savefig('device_usage.png')

    # 绘制图形
    plt.show()

if __name__ == '__main__':
    snmp_matplotlib_line(stime='2019-12-02 03:12:30')
    # print(select_tab(stime='2019-12-02 03:12:30'))
