# -*- coding: utf-8 -*-

from ftplib import FTP
import time
import os


#监控上传下载文件百分比 进度
class FtpUploadTracker():
    sizeWritten = 0
    totalSize = 0
    lastShownPercent = 0

    def __init__(self, totalSize):
        self.totalSize = totalSize

    def handle(self,block):
        file_handler.write(block)
        self.sizeWritten += 1024
        percentComplete = round((self.sizeWritten / self.totalSize) * 100)

        if (self.lastShownPercent != percentComplete):
            self.lastShownPercent = percentComplete
            return print(str(percentComplete) + " percent complete")


ftp = FTP('1.1.1.1')
ftp.encoding = 'utf-8'
ftp.login('admin','admin')
time.sleep(1)
print(ftp.getwelcome())
ftp.pwd()

#创建文件夹：
#ftp.mkd('2018-Swith-OS/HW/CE12800-V200R005C10SPC800')
ftp.cwd('2018-Swith-OS/HW/CE12800-V200R002C50SPC800/')
print(ftp.pwd())
print(ftp.retrlines('LIST'))

'''
#上传文件
file_put = 'C:\\ftp_file\\CE12800-V200R005C10SPC800.zip'# /的转义
fp = open(file_put,'rb')
cmd_001 = 'STOR CE12800-V200R005C10SPC800.zip'
uploadTracker = FtpUploadTracker(int(os.path.getsize(file_put)))
ftp.storbinary(cmd_001,fp,blocksize=1024,callback=uploadTracker.handle(block=1024))
fp.close()
'''

#下载文件
ftp.nlst()
#file_get = '/Users/shuang/PycharmProjects/NetDevOps_001/temp_file/CE12800-V200R002C50SPC800.cc'
file_get = 'C:\\Users\\liushuang\\PycharmProjects\\NetDevOps_001\\temp_file\\CE12800-V200R002C50SPC800.cc'
file_get_from = 'CE12800-V200R002C50SPC800.cc'
file_handler = open(file_get, 'wb')
cmd_002 = 'RETR '+file_get_from
print(ftp.size(file_get_from))
uploadTracker = FtpUploadTracker(int(ftp.size(file_get_from)))
ftp.retrbinary(cmd_002,blocksize=1024,callback=uploadTracker.handle)
file_handler.close()

ftp.quit()

