from http.server import HTTPServer, CGIHTTPRequestHandler

port = 80
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()

port_infor = os.popen('netstat -ano|findstr "80"').read().split('\n')

for i in port_infor:
    print(i)
