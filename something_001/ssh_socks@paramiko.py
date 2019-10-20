# -*- coding:utf-8 -*-
#https://pypi.org/project/PySocks/
import paramiko
import socks


s = socks.socksocket()
s.setproxy(
    socks.PROXY_TYPE_SOCKS5,'127.0.0.1',1089)

s.connect(('10.191.144.4',22))


# 设置全局代理
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',1088)
#socket.socket = socks.socksocket

# 解除代理
#socks.setdefaultproxy()
#socket.socket = socks.socksocket


# 实例化一个transport对象
trans = paramiko.Transport(s)
# 建立连接
trans.connect(username='ro', password='ro@ucloud.cn')

# 将sshclient的对象的transport指定为以上的trans
ssh = paramiko.SSHClient()
ssh._transport = trans
# 执行命令，和传统方法一样,简单交互，多次执行
cli_input = input("please input comm:")

stdin, stdout, stderr = ssh.exec_command(cli_input + ' | no-more')
print (stdout.read().decode())
print()
while True:
    cli_input = input("please input comm:")
    stdin, stdout, stderr = ssh.exec_command(cli_input + ' | no-more')
    print (stdout.read().decode())
    if cli_input =="q" or 'quit':
        break
# 关闭连接
trans.close()

