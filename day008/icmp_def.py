#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/10/31 14:02
# @Author: max liu
# @File  : icmp_def.py

import logging

from scapy.all import *

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


def ping_pro(ip):
    ping_pkt = IP(dst='196.21.5.254') / ICMP(type=8, code=0)  # 制造一个Ping包

    ping_result = sr1(ping_pkt, timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result
    ping_result.show()  # 查看回显结果


if __name__ == '__main__':
    ping_pro('127.0.0.1')
