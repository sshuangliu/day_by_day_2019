
import re
import time
import os

# # 运行一个简单的HTTP服务器
# from http.server import HTTPServer, CGIHTTPRequestHandler
#
# port = 80
# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
# print('Starting simple httpd on port: ' + str(httpd.server_port))
# httpd.serve_forever()




# 监控80端口

init_value = True
while init_value:
    time.sleep(1)
    print('等待一秒重新检测')
    port_infor = os.popen('netstat -ltnp').read().split('\n')
    for port_infor_001 in port_infor:
        if re.findall(r'tcp', port_infor_001,re.I) and re.findall(r'80\s', port_infor_001):
            print(r'HTTP (TCP/80)服务已打开')
            init_value = False
            break


