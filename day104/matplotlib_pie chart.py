#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/20 22:24
# @Author: max liu
# @File  : matplotlib_pie chart.py


from matplotlib import pyplot as plt
import matplotlib

print(matplotlib.matplotlib_fname())
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'


def pie_chart(size_list,name_list):
    #
    plt.figure(figsize=(6,6))


    explode = (0.01,0.01,0.01,0.01)

    patches , lable_text, percent_text = plt.pie(size_list,
                                                 explode=explode,
                                                 labels=name_list,
                                                 labeldistance=1.1,
                                                 autopct='%3.1f%%',
                                                 shadow=False,
                                                 startangle=90,
                                                 pctdistance=0.6
                                                 )
    for l in lable_text:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20

    plt.axis('equal')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    counters = [30,53,12,45]
    protocols = ['http','rdp','ftp','other']
    pie_chart(counters,protocols)