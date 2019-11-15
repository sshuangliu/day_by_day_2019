#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/15 12:55
# @Author: max liu
# @File  : config_to_db.py

import re
import hashlib
import sqlite3
import time
from day011.device_ssh_get_config import Device_ssh_001
import sys


class Config_comparison_and_to_db(Device_ssh_001):

    # def __init__(self, ip, username, password, cmd='show run'):  # dis cur
    #     super().__init__(ip, username, password)
    #     self.cmd = cmd

    def create_tab(self):
        conn = sqlite3.connect('running_configure_db.sqlite3')
        c = conn.cursor()

        #  创建表
        sql = '''
            CREATE TABLE running_configure_Backup(
            ID INTEGER PRIMARY KEY     AUTOINCREMENT,
			tdate TEXT,
            MD5_Value TEXT,
			RUN_CONFIG TEXT)
            '''

        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def insert_tab(self, date, md5_value, run_config):
        conn = sqlite3.connect('running_configure_db.sqlite3')
        c = conn.cursor()

        #  插入表
        sql = '''INSERT INTO running_configure_Backup(tdate,MD5_Value,RUN_CONFIG) VALUES (?,?,?)'''
        c.execute(sql, (date, md5_value, run_config))
        conn.commit()
        c.close()
        conn.close()

    def update_tab(self, date, md5_value, run_config, md5_value_before):
        conn = sqlite3.connect('running_configure_db.sqlite3')
        c = conn.cursor()

        #  更新表
        sql = '''UPDATE running_configure_Backup SET tdate = ?,MD5_Value = ?,RUN_CONFIG = ? WHERE MD5_Value = ?'''
        c.execute(sql, (date, md5_value, run_config, md5_value_before))
        conn.commit()
        c.close()
        conn.close()

    def select_tab(self, column='*'):
        conn = sqlite3.connect('running_configure_db.sqlite3')
        c = conn.cursor()

        #  查询表
        # sql = '''SELECT ? FROM running_configure_Backup'''  # 教主 在select后的的 这种占位符不行吗？？
        sql = f'''SELECT {column} FROM running_configure_Backup'''
        # results = c.execute(sql, (column,))
        results = c.execute(sql)
        results_all = results.fetchall()
        return results_all
        conn.commit()
        c.close()
        conn.close()

    def monitor_config_change_and_to_db(self):
        try:
            while True:
                m = hashlib.md5()
                cisco_return_values = re.search(r'hostname(.*)end', Device_ssh_001.ssh_get_config(self),
                                                re.DOTALL).group(1)
                m.update(cisco_return_values.encode())
                cisco_md5_values = m.hexdigest()
                if not self.select_tab():
                    self.insert_tab(time.strftime('%Y-%m-%d %H:%M:%S'), cisco_md5_values, cisco_return_values)
                    print('insert 条目：', cisco_md5_values)
                else:
                    if cisco_md5_values != self.select_tab('MD5_Value')[0][0]:
                        print(f'update 旧条目{self.select_tab("MD5_Value")[0][0]}为：{cisco_md5_values}')
                        self.update_tab(time.strftime('%Y-%m-%d %H:%M:%S'), cisco_md5_values, cisco_return_values,
                                        self.select_tab('MD5_Value')[0][0])
                    else:
                        print('无需更新，DB当前md5_value为：', self.select_tab('MD5_Value')[0][0])
                time.sleep(5)
        except KeyboardInterrupt: #
            sys.exit()


if __name__ == '__main__':
    test_change = Config_comparison_and_to_db(ip='192.168.59.136', username='cisco', password='Cisc0123')
    # print(test_change.ssh_get_config())
    test_change.create_tab()
    test_change.monitor_config_change_and_to_db()
