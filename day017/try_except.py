#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/16 12:13
# @Author: max liu
# @File  : try_except.py
import paramiko

from day011.device_ssh_get_config import Device_ssh_001
from day010.device_ping import ping_pro


# 自定义异常类
class Networktimeout_error(Exception):
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return repr(self.values)  # 把 任何 obj 转换为str 字符串，例如dict list


class Invalid_autocommand(Exception):
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return repr(self.values)  # 把 任何 obj 转换为str 字符串，例如dict list


class Enhance_device_ssh(Device_ssh_001):

    def device_ssh_new(self):
        try:
            if not ping_pro(self.ip): # 如果不通
                raise Networktimeout_error('连接超时 timeout')
            else:
                if 'invalid autocommand' in self.ssh_get_config():  # 非paramiko异常，正常输出，需要通过关键字判断 并转换为自定义异常
                    raise Invalid_autocommand('Line has invalid autocommand "show run"')
                else:
                    return self.ssh_get_config()
        except paramiko.ssh_exception.AuthenticationException as e:
            print(f'认证失败： {e}')

        except paramiko.ssh_exception.NoValidConnectionsError as e:
            print(f'SSH 请求被管理过滤： {e}')

        except Networktimeout_error as e:
            print(f'网络连通性失败： {e}')

        except Invalid_autocommand as e:
            print(f'输入命令有误或权限不够： {e}')


if __name__ == '__main__':
    get_config = Enhance_device_ssh(ip='192.168.59.137', username='cisco', password='Cisc0123')
    print(get_config.device_ssh_new())
