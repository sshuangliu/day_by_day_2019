#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/10/31 14:02
# @Author: max liu
# @File  : icmp_def.py

import logging
from kamene.all import *

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


# show_interfaces() 查看网卡list for windows
# get_if_list() 查看网卡list for Linux
def ping_pro(ip):
    ping_pkt = IP(dst=ip) / ICMP(type=8, code=0)  # 制造一个Ping包

    ping_result = sr1(ping_pkt, timeout=2, verbose=False,
                      iface='Intel(R) Dual Band Wireless-AC 7265')  # Ping并且把返回结果复制给ping_result
    ping_result.show()  # 查看回显结果


if __name__ == '__main__':
    ping_pro('114.114.114.114')
