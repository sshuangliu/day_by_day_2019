#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/18 16:46
# @Author: max liu
# @File  : ipv6_address.py

# http://tools.ietf.org/html/rfc4291#section-2.5.1 ipv6编址
# https://www.runoob.com/python3/python3-basic-operators.html 运算符

# 任何进制转十进制 int，10进制转其他进制
int('oxf', 16)
int('01010', 2)
hex(15)
bin(4)
oct(2)

# a = 0011 1100
#
# b = 0000 1101
# &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
# |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
# ^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
# ~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
# <<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
# >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数，低位丢弃	a >> 2 输出结果 15 ，二进制解释： 0000 1111

import ipaddress
import re


# 转换为完整的IPv6地址
def full_ipv6(ipv6):
    return ipaddress.ip_address(ipv6).exploded


print(full_ipv6('2001::4b2:4aff:fe00:9f'))


#  low-order 24 bits of an address
#    (unicast or anycast) and appending those bits to the prefix
#    FF02:0:0:0:0:1:FF00::/104 resulting in a multicast address in the
#    range
#
#          FF02:0:0:0:0:1:FF00:0000
#
#    to
#
#          FF02:0:0:0:0:1:FFFF:FFFF
#   For example, the Solicited-Node multicast address corresponding to
#   the IPv6 address 4037::01:800:200E:8C6C is FF02::1:FF0E:8C6C


def solicited_node_multicast_address(ipv6):
    return "FF02::1:FF" + full_ipv6(ipv6)[-7:]  # -7 包括了一个":", 拼接得到Solicited_node_multicast_address


print(solicited_node_multicast_address('2001::4b2:4aff:fe00:9f'))


def mac_to_ipv6_linklocal(mac):
    # 移除多余的字符 空格,冒号,点,减号
    # 转换16进制数到10进制数
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    # 00:50:56:ab:4d:19为例

    # high2 使用移位">> 32"得到0050,
    # 使用"& 0xffff"确认只有4个16进制数,
    # 使用"^ 0x200"异或转换第七位,得到0250
    # 异或算法
    # >>> 0 ^ 1
    # 1
    # >>> 1 ^ 1
    # 0
    # high2 = 0250(其实是10进制,而不是这里显示的16进制)
    high2 = mac_value >> 32 & 0xffff ^ 0x0200  # 0x2 = 0b00000010
    # high1 使用移位">> 24"得到005056,
    # 使用"& 0xff"得到最后两个16进制数,56
    # high1 = 56(其实是10进制,而不是这里显示的16进制)
    high1 = mac_value >> 24 & 0xff
    # low1 使用移位">> 16"得到005056ab,
    # 使用"& 0xff"得到最后两个16进制数,ab
    # low1 = ab(其实是10进制,而不是这里显示的16进制)
    low1 = mac_value >> 16 & 0xff
    # low2 使用"& 0xffff"得到最后4个16进制数,4d19
    # low2 = 4d19(其实是10进制,而不是这里显示的16进制)
    low2 = mac_value & 0xffff

    # 使用格式化打印,转换10进制位16进制,x为16进制字符串,并且使用02和04在控制长度,并且补0
    return 'fe80::{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(high2, high1, low1, low2)


# 获取EUI64地址 及包含EUI64的full ipv6地址 包括link-local, prefix FE80::/10
def mac2eui64(mac, prefix=None):
    """
    Convert a MAC address to a EUI64 address
    or, with prefix provided, a full IPv6 address
    """
    eui64 = re.sub(r'[.:-]', '', mac).lower()
    eui64 = eui64[0:6] + 'fffe' + eui64[6:]
    # print(hex(int(eui64[0:2], 16) ^ 2))  # 打印结果为： 0x4
    eui64 = hex(int(eui64[0:2], 16) ^ 2)[2:].zfill(2) + eui64[2:]  # zfill(n) 返回指定长度的字符串 右对齐 前面填充0
    if prefix is None:
        return ':'.join(re.findall(r'.{4}', eui64))
    else:
        try:
            net = ipaddress.ip_network(prefix, strict=False)  # False 如果输入地址有主机位，则置0
            euil = int('0x{0}'.format(eui64), 16)
            return str(net[euil])  # EUI64位主机位，直接从网络主机列表属性提取
        except  Exception:  # pylint: disable=bare-except
            return


print(mac2eui64(mac='06:b2:4a:00:00:9f'))
print(mac2eui64(mac='06:b2:4a:00:00:9f', prefix='2001:db8:100::/64'))
print(mac2eui64(mac='06:b2:4a:00:00:9f', prefix='FE80::/10'))


# 获取EUI64地址 及包含EUI64的full ipv6地址 包括link-local, prefix FE80::/10
def eui642mac(ipv6):
    """
    Convert a IPV6 address with contains EUI64 to MAC address
    """
    full_ipv6 = ipaddress.ip_address(ipv6).exploded
    eui64 = re.sub(r':', '', full_ipv6).lower()[-16:]
    eui64 = eui64[0:6] + eui64[-6:]
    # print(hex(int(eui64[0:2], 16) ^ 2))  # 打印结果为： 0x6
    eui64 = hex(int(eui64[0:2], 16) ^ 2)[2:].zfill(2) + eui64[2:]  # zfill(n) 返回指定长度的字符串 右对齐 前面填充0
    return '-'.join(re.findall(r'.{4}', eui64))


print(eui642mac('2001::4b2:4aff:fe00:9f'))
print(eui642mac('fe80::4b2:4aff:fe00:9f'))

if __name__ == '__main__':
    pass
