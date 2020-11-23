'''
create time : 11/23/20 02:43 
author : hcai
'''

import optparse
import socket
import socketserver
import codecs
import time

header = '''HTTP/1.1 200 OK\r
Server: Microsoft-IIS/6.0\r
Content-Type: text/html
Connection: close\r\n\r\n'''

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        s = header + "payload-for-test"
        time.sleep(0.5)
        all_bytes = codecs.encode(s.encode('utf-8'), 'hex')
        self.request.sendall(codecs.decode(all_bytes, 'hex'))

def start_http_server():
    server = socketserver.TCPServer((host, port), MyTCPHandler)
    server.serve_forever()

if __name__ == '__main__':
    myParser = optparse.OptionParser()
    myParser.add_option("-t", "--host", help="server host ip", default = None)
    myParser.add_option("-p", "--port", help="server port number")
    myParser.add_option("-f", "--file", help="the file to be sent")
    (opts, args) = myParser.parse_args()

    # set the host ip
    host = opts.host
    if not host:
        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)

    # For http, port number is 80
    port = opts.port
    if not port:
        port = 80
    port = int(port)

    start_http_server()
