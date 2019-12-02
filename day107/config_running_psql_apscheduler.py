#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/1 10:42
# @Author: max liu
# @File  : config_running_psql_apscheduler.py


import re
import hashlib
from day011.device_ssh_get_config import Device_ssh_001
import pg8000
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import logging
from datetime import datetime

#  2019-11-28 15:44:11 base.py[line:440] INFO Adding job tentatively -- it will be properly scheduled when the scheduler starts
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='apscheduler_monitor_config_change_and_to_db_.log',
                    filemode='a')


class Config_comparison_and_to_db(Device_ssh_001):

    # def __init__(self, ip, username, password, cmd='show run'):  # dis cur
    #     super().__init__(ip, username, password)
    #     self.cmd = cmd

    def create_tab(self):
        conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                              database='shuangdb_001')
        c = conn.cursor()

        #  创建表
        sql = '''
            CREATE TABLE running_configure_Backup(
            ID SERIAL PRIMARY KEY,
			tdate timestamp default current_timestamp,
            MD5_Value TEXT,
			RUN_CONFIG TEXT)
            '''

        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def insert_tab(self, md5_value, run_config):
        conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                              database='shuangdb_001')
        c = conn.cursor()

        #  插入表
        sql = f'''INSERT INTO running_configure_Backup(MD5_Value,RUN_CONFIG) VALUES ('{md5_value}','{run_config}')'''  # 参数需要''  艹！！！！！！！！！
        # sql = '''INSERT INTO running_configure_Backup(MD5_Value,RUN_CONFIG) VALUES ('%s','%s')''' % (md5_value, run_config)
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def update_tab(self, date, md5_value, run_config, md5_value_before):
        conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                              database='shuangdb_001')
        c = conn.cursor()

        #  更新表
        sql = f'''UPDATE running_configure_Backup SET tdate = '{date}',MD5_Value = '{md5_value}',RUN_CONFIG = '{run_config}' WHERE MD5_Value = '{md5_value_before}' ''' # 参数需要''  艹！！！！！！！！！
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def select_tab(self, column='*'):
        conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                              database='shuangdb_001')
        c = conn.cursor()

        #  查询表
        sql = f'''SELECT {column} FROM running_configure_Backup'''  # 列名又不需要'' 艹！！！！
        results = c.execute(sql)
        results_all = results.fetchall()
        return results_all
        conn.commit()
        c.close()
        conn.close()

    def monitor_config_change_and_to_db(self):
        m = hashlib.md5()
        cisco_return_values = re.search(r'hostname(.*)end', Device_ssh_001.ssh_get_config(self),
                                        re.DOTALL).group(1)
        m.update(cisco_return_values.encode())
        cisco_md5_values = m.hexdigest()
        if not self.select_tab():
            self.insert_tab(cisco_md5_values, cisco_return_values)
            print('insert 条目：', cisco_md5_values)
        else:
            if cisco_md5_values != self.select_tab('MD5_Value')[0][0]:
                print(f'update 旧条目{self.select_tab("MD5_Value")[0][0]}为：{cisco_md5_values}')
                self.update_tab(datetime.now(), cisco_md5_values, cisco_return_values,
                                self.select_tab('MD5_Value')[0][0])
            else:
                print('无需更新，DB当前md5_value为：', self.select_tab('MD5_Value')[0][0])


def my_listener(event):
    if event.exception:
        print('任务出错了！！！！！！')
    else:
        print('任务照常运行:周期性监控设备配置变化...3秒一次')


if __name__ == '__main__':
    test_change = Config_comparison_and_to_db(ip='192.168.59.138', username='cisco', password='Cisc0123')
    # print(test_change.ssh_get_config())
    # test_change.create_tab()
    # test_change.monitor_config_change_and_to_db()
    scheduler = BlockingScheduler()
    # scheduler.add_job(func=date_test, args=('一次性任务,会出错',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15), id='date_task')

    scheduler.add_job(func=test_change.create_tab, args=[], trigger='date', run_date='2019-12-01 13:56:00', id='once_task') # 被调度函数参数由args传入，列表 元组都可
    scheduler.add_job(func=test_change.monitor_config_change_and_to_db, args=[], trigger='interval', seconds=3, start_date='2019-12-01 13:56:30', id='interval_task')
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler._logger = logging

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        exit()
