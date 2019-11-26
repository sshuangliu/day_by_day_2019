#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/9 17:51
# @Author: max liu
# @File  : new_ping_class.py

from day013.ping_class import Shuang_ping
from kamene.all import *

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


class New_ping(Shuang_ping):

    def __pkt_for_icmp(self):  # single_leading_underscore 私有方法,仅仅在内部调用 模块导入也到其他也无法使用
        ping_pkt = IP(dst=self.dstip, src=self.srcip) / ICMP(type=8, code=0) / (b'P' * self.length)  # 制造一个Ping包
        return ping_pkt

    def ping(self):
        for i in range(0, 5):
            ping_result = sr1(self.__pkt_for_icmp(), timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result
            # ping_result.show()  # 查看回显结果
            # print(ping_result[ICMP].show())
            try:
                if (ping_result[ICMP].type == ping_result[ICMP].code == 0) and (ping_result.getlayer(IP).fields.get(
                        'src') == self.__pkt_for_icmp().getlayer(IP).fields.get('dst')):
                    print('+', end='')
            except TypeError:
                print('?', end='')
        print()

if __name__ == '__main__':
    ping = Shuang_ping('192.168.157.2')
    total_lenth = 70


    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((total_lenth - len(word)) / 2), word, s * int((total_lenth - len(word)) / 2)))


    print_new('print class')
    print(ping)

    print_new('ping one for sure reachable')
    ping.one()

    print_new('ping five')
    ping.ping()

    print_new('set payload length')
    ping.length = 200
    print(ping)
    ping.ping()

    print_new('set ping src ipadd')
    ping.srcip = '8.8.8.8'
    print(ping)
    ping.ping()

    print_new('New class Newping', '=')
    newping = New_ping('192.168.157.2')
    newping.length = 300
    print(newping)
    newping.ping()
