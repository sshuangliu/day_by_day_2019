#!/usr/bin/env python
import paramiko
import time

ip = "192.168.59.132"
username = "cisco"
password = "Cisc0123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh_client.connect(hostname=ip,username=username,password=password)

print("Sucessfully login to ", ip)

command = ssh_client.invoke_shell()
command.send("configure terminal\n")
command.send("int loop 0\n")
command.send("ip address 1.1.1.2 255.255.255.255\n")
command.send("end\n")
command.send("wr mem\n")
time.sleep(1)
output = command.recv(65535).decode()
print(output)
ssh_client.close
print()
