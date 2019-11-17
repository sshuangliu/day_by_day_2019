#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/17 12:07
# @Author: max liu
# @File  : scapy_arp_gratuitous.py


import logging
from kamene.all import *

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


# show_interfaces() 查看网卡list for windows
# get_if_list() 查看网卡list for Linux
def arp_gratuitous():
    ping_pkt = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(op=2, hwsrc='00:0c:29:d1:e0:49', psrc='192.168.59.100',
                                                    hwdst='00:0c:29:d1:e0:49', pdst='192.168.59.100')  # 有些字段不需填写
    ping_pkt.show()
    ping_result = srp1(ping_pkt, iface='ens37', timeout=2, verbose=True)  # Ping并且把返回结果复制给ping_result
    # ping_result.show()  # 查看回显结果
    # print(ping_result[ICMP].show())


if __name__ == '__main__':
    arp_gratuitous()
