#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/9 17:30
# @Author: max liu
# @File  : ping_class.py

import logging
from kamene.all import *

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


class Shuang_ping:
    def __init__(self, dstip=None, length=100, srcip=None):
        self.length = length
        self.srcip = srcip
        self.dstip = dstip

    def __str__(self):
        if not self.srcip:
            return f'<{self.__class__.__name__}=> dstip: {self.dstip}, size: {self.length}>'
        elif self.srcip:
            return f'<{self.__class__.__name__}=> srcip: {self.srcip}, dstip: {self.dstip}, size: {self.length}>'

    def __pkt_for_icmp(self):  # 私有方法,仅仅在内部调用 模块导入也到其他也无法使用
        ping_pkt = IP(dst=self.dstip, src=self.srcip) / ICMP(type=8, code=0) / (b'P' * self.length)  # 制造一个Ping包
        return ping_pkt

    def one(self): #### 为啥结果 多余返回了一个None，排查了半天没看出来，教主帮忙看看？
        # self.__pkt_for_icmp().show()
        ping_result = sr1(self.__pkt_for_icmp(), timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result
        # ping_result.show()  # 查看回显结果
        # print(ping_result[ICMP].show())
        try:
            if (ping_result[ICMP].type == ping_result[ICMP].code == 0) and (ping_result.getlayer(IP).fields.get(
                    'src') == self.__pkt_for_icmp().getlayer(IP).fields.get('dst')):
                print('%s 可达！' % self.dstip)
        except TypeError:
            print('%s 不可达！' % self.dstip)

    def ping(self):
        for i in range(0, 5):
            ping_result = sr1(self.__pkt_for_icmp(), timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result
            # ping_result.show()  # 查看回显结果
            # print(ping_result[ICMP].show())
            try:
                if (ping_result[ICMP].type == ping_result[ICMP].code == 0) and (ping_result.getlayer(IP).fields.get(
                        'src') == self.__pkt_for_icmp().getlayer(IP).fields.get('dst')):
                    print('!', end='')
            except TypeError:
                print('.', end='')
        print()


if __name__ == '__main__':
    pass
