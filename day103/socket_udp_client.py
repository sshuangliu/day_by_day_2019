#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-11-19 20:40
#@Author: max liu
#@File  : socket_udp_client.py


import socket
import pickle
import struct

def udp_client(ip, port, data_list):
    """
    version  2byte
    pkt_type 2byte
    seq_id   4byte
    lengths  4byte
    md5      16byte
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ip, port
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        send_data = pickle.dumps(x)
        lengths = len(send_data)+12
        protocpl_fields = struct.pack('>HHLL',version,pkt_type,seq_id,lengths)
        s.sendto(protocpl_fields+send_data, address)
    s.close()


if __name__ == '__main__':
    data_list = ['333tuuu', 123456789, {testv: 87076677}, [1, 2, 3], True]

