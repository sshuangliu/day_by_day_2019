# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/15 16:43
# @Author: max liu
# @File  : test_unit.py

import signal
import sys
import time


def signal_handler(signal, frame):
    print('Press Ctrl+C')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
while True:
    time.sleep(1)


