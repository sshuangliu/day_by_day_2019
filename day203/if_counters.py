#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/20 21:35
#@Author: max liu
#@File  : if_counters.py

from cli import *
import sys, time

# 收集客户输入的第一个参数 接口名
ifName = sys.argv[1]
# 收集客户输入的第二个参数 延时
delay = float(sys.argv[2])
# 收集客户输入的第三个参数 数量
count = int(sys.argv[3])
# 产生查看特定接口计数器counters信息的命令
cmd = 'show interface ' + ifName + ' counters'

# 执行命令
out = json.loads(clid(cmd))
# >>> from cli import *
# >>> print(json.loads(clid('show interface e1/1 counters')))
# {u'TABLE_rx_counters': {u'ROW_rx_counters': [{u'eth_inucast': u'0', u'eth_inbytes': u'0', u'interface_rx': u'Ethernet1/1'},
#                                              {u'eth_inmcast': u'0', u'interface_rx': u'Ethernet1/1', u'eth_inbcast': u'0'}]},
#  u'TABLE_tx_counters': {u'ROW_tx_counters': [{u'eth_outucast': u'0', u'interface_tx': u'Ethernet1/1', u'eth_outbytes': u'0'},
#                                              {u'eth_outmcast': u'0', u'eth_outbcast': u'0', u'interface_tx': u'Ethernet1/1'}]}}

# 提取入向和出向,单播,组播和广播的数量
rxuc = int(out['TABLE_rx_counters']['ROW_rx_counters'][0]['eth_inucast'])
rxmc = int(out['TABLE_rx_counters']['ROW_rx_counters'][1]['eth_inmcast'])
rxbc = int(out['TABLE_rx_counters']['ROW_rx_counters'][1]['eth_inbcast'])
txuc = int(out['TABLE_tx_counters']['ROW_tx_counters'][0]['eth_outucast'])
txmc = int(out['TABLE_tx_counters']['ROW_tx_counters'][1]['eth_outmcast'])
txbc = int(out['TABLE_tx_counters']['ROW_tx_counters'][1]['eth_outbcast'])

# 打印输出
print 'row rx_ucast rx_mcast rx_bcast tx_ucast tx_mcast tx_bcast'
print '========================================================='
print '    %8d %8d %8d %8d %8d %8d' % (rxuc, rxmc, rxbc, txuc, txmc, txbc)
print '========================================================='

i = 0
while i < count:  # 循环客户输入的次数
    time.sleep(delay)  # 每一次增加客户输入的延时
    out = json.loads(clid(cmd))
    rxucNew = int(out['TABLE_rx_counters']['ROW_rx_counters'][0]['eth_inucast'])
    rxmcNew = int(out['TABLE_rx_counters']['ROW_rx_counters'][1]['eth_inmcast'])
    rxbcNew = int(out['TABLE_rx_counters']['ROW_rx_counters'][1]['eth_inbcast'])
    txucNew = int(out['TABLE_tx_counters']['ROW_tx_counters'][0]['eth_outucast'])
    txmcNew = int(out['TABLE_tx_counters']['ROW_tx_counters'][1]['eth_outmcast'])
    txbcNew = int(out['TABLE_tx_counters']['ROW_tx_counters'][1]['eth_outbcast'])
    i += 1
    print '%-3d %8d %8d %8d %8d %8d %8d' % \
    (i, rxucNew - rxuc, rxmcNew - rxmc, rxbcNew - rxbc, txucNew - txuc, txmcNew - txmc, txbcNew - txbc)