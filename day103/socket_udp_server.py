#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-11-19 22:40
# @Author: max liu
# @File  : socket_udp_server.py


import struct
import socket
import pickle
import sys
import hashlib


def udp_server(ip, port):
    """
    version  2byte
    pkt_type 2byte
    seq_id   4byte
    lengths  4byte
    md5      16byte
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip, port))
    print('udp server done')
    while True:
        try:
            data, add = s.recvfrom(1024)
            protocol_fields = struct.unpack('>HHLL', data[:12])
            data_recv = pickle.loads(data[12:protocol_fields[3]])  # total_lengths-protocol_lengths
            md5_value_recv = data[-32:].decode()
            m = hashlib.md5()
            m.update(data[:protocol_fields[3]])
            md5_value = m.hexdigest()
            if md5_value == md5_value_recv:
                print('=' * 80)
                print("{0:<30}:{1:<30}".format('发送自', str(add)))
                print("{0:<30}:{1:<30}".format('序列ID', protocol_fields[2]))
                print("{0:<30}:{1:<30}".format('total长度', protocol_fields[3]))
                print("{0:<30}:{1:<30}".format('数据', str(data_recv)))

        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    udp_server('192.168.59.37', 6666)
