#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/5 9:16
# @Author: max liu
# @File  : syslog_trap_to_psql.py


import logging
import socketserver
import re
from dateutil import parser
import pg8000

LOG_FILE = 'syslog_trap.log'

# 配置logging.info, 记录文件到本地
logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    datefmt='',
                    filename=LOG_FILE,  # log文件
                    filemode='a')  # 追加模式

# facility与ID的对应关系的字典
facility_dict = {0: 'KERN',
                 1: 'USER',
                 2: 'MAIL',
                 3: 'DAEMON',
                 4: 'AUTH',
                 5: 'SYSLOG',
                 6: 'LPR',
                 7: 'NEWS',
                 8: 'UUCP',
                 9: 'CRON',
                 10: 'AUTHPRIV',
                 11: 'FTP',
                 16: 'LOCAL0',
                 17: 'LOCAL1',
                 18: 'LOCAL2',
                 19: 'LOCAL3',
                 20: 'LOCAL4',
                 21: 'LOCAL5',
                 22: 'LOCAL6',
                 23: 'LOCAL7'}

# severity_level与ID的对应关系的字典
severity_level_dict = {0: 'EMERG',
                       1: 'ALERT',
                       2: 'CRIT',
                       3: 'ERR',
                       4: 'WARNING',
                       5: 'NOTICE',
                       6: 'INFO',
                       7: 'DEBUG'}


class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = bytes.decode(self.request[0].strip())  # 读取数据,原始数据为字节码
        logging.info(str(data))  # 把信息logging到本地, logging level为INFO

        # ============syslog字段分析器===============
        try:
            # 1 ：CSR1000V cisco like
            if re.match(r'^<(\d+)>(\d+): \*(.*): %(\w+)-(\d)-(\w+): (.*)$', data):
                syslog_infor = re.match(r'^<(\d+)>(\d+): \*(.*): %(\w+)-(\d)-(\w+): (.*)$', data).groups()
                facility_value = facility_dict[int(syslog_infor[0]) >> 3]  # 前五位二进制
                severity_level = severity_level_dict[(int(syslog_infor[0]) << 5 & 0xff) >> 5]  # 后三位二进制
                log_id = int(syslog_infor[1])
                log_time = parser.parse(syslog_infor[2]).strftime("%Y-%m-%d %H:%M:%S")
                log_type = syslog_infor[3]
                severity_level_too = severity_level_dict[int(syslog_infor[4])]
                log_type_op = syslog_infor[5]
                log_context = syslog_infor[6]

                conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                                      database='shuangdb_001')
                c = conn.cursor()

                #  插入表 字符值需要加‘’，数字不需要！！！！！！
                sql = f'''INSERT INTO syslog_trap_infor(device_ipadd,facility_value,severity_level,log_time,log_type,log_type_op,log_context) VALUES ('{self.client_address[0]}','{facility_value}', '{severity_level}', '{log_time}','{log_type}','{log_type_op}','{log_context}') '''  # 参数需要''  ！！！！！！！！！
                c.execute(sql)
                conn.commit()
                c.close()
                conn.close()
                print(data)

            # 2 ：others
            # elif :

            else:
                print(data)
                print('syslog格式不支持，待适配！')


        except AttributeError:
            pass


def create_tab():
    conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                          database='shuangdb_001')
    c = conn.cursor()
    #  创建表
    sql = '''
                        CREATE TABLE syslog_trap_infor(
                        ID SERIAL PRIMARY KEY,
                        device_ipadd inet not null ,
                        facility_value varchar(20) ,
                        severity_level varchar(20) ,
            			log_time timestamp ,
            			log_type varchar(20) ,
            			log_type_op varchar(20) ,
            			log_context text )
                        '''

    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    # create_tab()
    try:
        HOST, PORT = "0.0.0.0", 514  # 本地地址与端口
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)  # 绑定本地地址，端口和syslog处理方法
        print("Syslog 服务已启用, 写入日志到文本文件!!!")
        server.serve_forever(poll_interval=0.5)  # 运行服务器，和轮询间隔

    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:  # 捕获Ctrl+C，打印信息并退出
        print("Crtl+C Pressed. Shutting down.")

