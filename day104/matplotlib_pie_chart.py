#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/20 22:24
# @Author: max liu
# @File  : matplotlib_pie_chart.py


from matplotlib import pyplot as plt
import matplotlib

print(matplotlib.matplotlib_fname())
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'


def pie_chart(size_list,name_list):
    # 设置图片大小:长宽
    plt.figure(figsize=(6,6))

    # 爆炸出来每一部分，以及每部分之间的间隙
    explode = (0.01,0.01,0.01,0.01)

    # pie 饼状图的函数，有返回值. 传入参数：
    # size_list 各个部分的数值大小，会自动计算他们之间的相对百分比
    # explode 是否爆炸，可以不传入，则为None
    # labels 每部分的标签文字
    # labeldistance 标签文字距离圆心的半径倍数
    # autopct 扇形区域数值格式 3位整数，2位小数的百分数
    # shadow 是否有阴影
    # startangle 画图的起始角度，90度起始 逆时针绘制图形
    # pctdistance 百分比数值 距离圆心的半径倍数
    patches, lable_text, percent_text = plt.pie(size_list,
                                                 explode=explode,
                                                 labels=name_list,
                                                 labeldistance=1.1,
                                                 autopct='%3.2f%%',
                                                 shadow=False,
                                                 startangle=90,
                                                 pctdistance=0.6
                                                 )
    print(lable_text)
    print(percent_text)
    print(patches)
    # pie函数返回值 lable_text,percent_text ,如果需要改变文本大小，可以for遍历
    # 然后set_size设置其大小
    for l in lable_text:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20

    # 横纵坐标 比例相等，保证图形是圆的
    # plt.axis([-1, 10, 0, 6]) 横轴-1 10.纵轴0 6
    plt.axis('equal')
    plt.legend()
    plt.savefig('pie_chat.png', dpi=600)
    plt.show()

if __name__ == '__main__':

    counters = [30,53,12,45]
    protocols = ['http','rdp','ftp','other']
    pie_chart(counters, protocols)

