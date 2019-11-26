#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/23 22:35
# @Author: max liu
# @File  : matplotlib_netflow.py

from day009.paramiko_ssh_device import shuang_ssh
from matplotlib import pyplot as plt
import matplotlib
import re
import random


class Matplotlib_netflow(object):
    def __init__(self, ip, username, password, port=22,
                 cmd='show  flow monitor name qytang-monitor cache format table'):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.cmd = cmd

    def netflow_dict(self):
        netflow_return_value = shuang_ssh(self.ip, self.username, self.password, self.port, self.cmd)
        netflow_list = netflow_return_value.strip().splitlines()
        # print(netflow_list)
        netflow_app_name_list_start_index = \
            [i for i, element in enumerate(netflow_list) if element.find('APP NAME') != -1][
                0] + 2  # 列表元素模糊查询, 以'APP NAME'列为参考列
        netflow_app_name_dict = {}
        # print(netflow_list[netflow_app_name_list_start_index:])
        for app_rows in netflow_list[netflow_app_name_list_start_index:]:
            netflow_app_name_dict[re.split(r'\s+', app_rows.strip())[1]] = re.split(r'\s+', app_rows.strip())[-1]
        print(netflow_app_name_dict)
        return netflow_app_name_dict

    def netflow_pie_chart(self):
        netflow_protocol = []
        netflow_bytes = []
        for key, value in self.netflow_dict().items():
            netflow_protocol.append(key)
            netflow_bytes.append(int(value))

        plt.figure(figsize=(6, 6))
        explode = []
        for i in range(len(netflow_bytes)):
            explode.append(0.02)
        explode = tuple(explode)
        plt.pie(netflow_bytes,
                explode=explode,
                labels=netflow_protocol,
                labeldistance=1.1,
                autopct='%3.2f%%',
                shadow=False,
                startangle=90,
                pctdistance=0.6
                )
        plt.axis('equal')
        plt.legend()
        # plt.savefig('pie_chat.png', dpi=600)
        plt.show()

    def netflow_bar(self):
        netflow_protocol = []
        netflow_bytes = []
        for key, value in self.netflow_dict().items():
            netflow_protocol.append(key)
            netflow_bytes.append(int(value))

        colorlist = random.sample(list(matplotlib.colors.cnames.keys()), len(netflow_protocol))  # 148种颜色， 随机各个条形块的颜色
        # colorlist = random.sample(list(matplotlib.colors.cnames.values()), len(netflow_protocol))  # 148种颜色， 随机各个条形块的颜色
        print(colorlist)

        plt.figure(figsize=(6, 6))
        # 横向柱状图 长条宽度默认0.8
        # plt.barh(netflow_protocol, netflow_bytes, height=0.5, color=colorlist)

        # 竖向柱状图
        # x 长条形中点横坐标0,1,2...
        plt.bar(x=range(len(netflow_protocol)), height=netflow_bytes, width=0.5, color=colorlist)
        # plt.barh(x=range(len(netflow_protocol)), height=netflow_bytes, width=0.5) # 横向
        plt.xticks(range(len(netflow_protocol)), netflow_protocol)  # 设置X轴刻度对应的名称
        # plt.yticks(range(len(netflow_protocol)), netflow_protocol) #  设置y轴刻度对应的名称

        # 添加主题和注释
        plt.ylim(ymin=0)
        # plt.ylim(ymin=0,ymax=1000)  设置y轴坐标范围 ,原始数据y为int时才有效
        # plt.xlim(xmin=-100,xmax=100) 设置X轴坐标范围,原始数据x为int时才有效
        # 设置x,y四个最值，列表传入
        # plt.axis([-100, 100, 0, 10000])
        plt.title('flow monitor')  # 主题
        plt.xlabel('application name')  # X轴注释
        plt.ylabel('Total number of bytes')  # Y轴注释

        # x,y:表示坐标值上的值,条形图的中间点坐标为0,1,2,...
        for x, y in enumerate(netflow_bytes):
            plt.text(x, y + 10, '%s' % y, verticalalignment="bottom", horizontalalignment="center")

        # 保存到图片
        # plt.savefig('bar.png', dpi=600)
        # plt.savefig('barh.png', dpi=600)
        # 绘制图形
        plt.show()

    def random_color(self): #  148种颜色
        hex_colors_dic = {}
        rgb_colors_dic = {}
        hex_colors_only = []
        for name, hex in matplotlib.colors.cnames.items():  # 本身是个dict
            hex_colors_only.append(hex)  # color的十六进制list ['#F0F8FF',..., '#00FFFF']
            hex_colors_dic[name] = hex  # color的名字：十六进制 dict {'aliceblue': '#F0F8FF'...'antiquewhite': '#FAEBD7'}
            rgb_colors_dic[name] = matplotlib.colors.to_rgb(
                hex)  # color的名字 RGB的值 dict {'aliceblue': (0.9411764705882353, 0.9725490196078431, 1.0),...}
        return random.choice(hex_colors_only)


if __name__ == '__main__':
    nf = Matplotlib_netflow('192.168.59.138', 'cisco', 'Cisc0123')
    # nf.netflow_dict()
    # nf.netflow_pie_chart()
    nf.netflow_bar()
