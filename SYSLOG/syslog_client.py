#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/4 13:13
#@Author: max liu
#@File  : syslog_client.py

import socket


class Facility:
    # Syslog facilities
    KERN, USER, MAIL, DAEMON, AUTH, SYSLOG, LPR, NEWS, UUCP, CRON, AUTHPRIV, FTP = range(12)

    LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7 = range(16, 24)


class Level:
    # Syslog levels
    EMERG, ALERT, CRIT, ERR, WARNING, NOTICE, INFO, DEBUG = range(8)


class Syslog:
    # A syslog client that logs to a remote server.
    def __init__(self, host="localhost", port=514, facility=Facility.LOCAL7):
        self.host = host
        self.port = port
        self.facility = facility
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 如果使用send就需要给LEVEL
    def send(self, message, level):
        # Send a syslog message to remote host using UDP.
        data = "<%d>%s" % (level + self.facility * 8, message)
        self.socket.sendto(data.encode(), (self.host, self.port))
        print('********')
        print(level+self.facility*8)

    # 非send的方法,会使用默认LEVEL
    def warn(self, message):
        # Send a syslog warning message.
        self.send(message, Level.WARNING)

    def notice(self, message):
        # Send a syslog notice message.
        self.send(message, Level.NOTICE)

    def error(self, message):
        # Send a syslog error message.
        self.send(message, Level.ERR)


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    log = Syslog("192.168.59.37")
    log.send(" syslog test", Level.NOTICE)
    log.error("syslog test")