#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-11-19 20:40
# @Author: max liu
# @File  : socket_udp_client.py


import socket
import pickle
import struct
import hashlib


def udp_client(ip, port, data_list):
    """
    version  2byte
    pkt_type 2byte
    seq_id   4byte
    lengths  4byte
    md5      16byte  #  教主  超过long long int 8字节大小  按整数struck.pack() 如何操作？
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ip, port
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        send_data = pickle.dumps(x)
        total_lengths = len(send_data) + 12
        protocol_fields = struct.pack('>HHLL', version, pkt_type, seq_id, total_lengths)
        m = hashlib.md5()
        m.update(protocol_fields + send_data)
        md5_value = m.hexdigest()
        s.sendto(protocol_fields + send_data + md5_value.encode(), address)
        seq_id += 1
    s.close()


if __name__ == '__main__':
    data_list = ['333tuuu', 123456789, {'testv': 87076677}, [1, 2, 3], True]
    udp_client('192.168.59.37', 6666, data_list)
