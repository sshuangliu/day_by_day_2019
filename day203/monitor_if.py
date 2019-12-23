#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/20 21:36
#@Author: max liu
#@File  : monitor_if.py

#cisco 内置调度器
'''
feature scheduler
scheduler job name run_python
  python bootflash:/scripts/monitor_if.py
  exit

scheduler schedule name sch_run_python
  job name run_python
  time start 2019:12:20:14:40 repeat 0:0:1

show scheduler schedule
'''

# cisco eem
'''
event manager applet eg-2
  event snmp oid 1.3.6.1.4.1.9.9.109.1.1.1.1.6.1 get-type exact entry-op ge entr
y-val 0 poll-interval 3
  action 1.0 cli source monitor_if.py -r

'''

from cisco.interface import *
from nxos import *

"""
周期性调度:
feature scheduler 
scheduler job name run_python
    python bootflash:///3_monitor_if.py
    exit
scheduler schedule name schedule_run_python
    job name run_python
    time start now repeat 0:0:1
    end

查看日志:
NXOS1# show logging logfile 
2018 Sep  8 01:07:02 NXOS1  %USER-3-SYSTEM_MSG: Interface state is up! - nxpython
2018 Sep  8 01:12:07 NXOS1  %USER-3-SYSTEM_MSG: Interface state is up! - nxpython
2018 Sep  8 01:14:11 NXOS1  %USER-3-SYSTEM_MSG: Interface state is down!, try to no shutdown! - nxpython
"""
# 产生接口实例
lo0 = Interface('loopback0')
# 判断接口是否Down
if lo0.show().admin_state == 'down':
    # 如果接口处于down的状态,就重新打开接口,并且产生系统日志
    lo0.set_state(s="up")
    py_syslog(3, 'Interface state is down!, try to no shutdown!')
else:  # 如果接口处理up状态,依然产生正常的系统日志
    py_syslog(3, 'Interface state is up!')
