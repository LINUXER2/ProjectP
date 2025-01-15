import http.server
import socketserver
from base64 import b64encode
from datetime import datetime
from json import dumps
from socket import socket, SOCK_STREAM, AF_INET
from threading import Thread

from http_server import localIp


def init_socket_sync():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('172.19.39.154', 6789))
    server.listen(512)
    print('服务器启动监听...')
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        client.send(str(datetime.now()).encode('utf-8')),
        client.close()


class FileTransHandler(Thread):
    def __init__(self, client):
        super().__init__()
        self.client = client

    def run(self):
        with open('baidu.png', 'rb') as file:
            data = b64encode(file.read()).decode('utf-8')
        my_dict = {}
        my_dict['fileName'] = 'baidu.png'
        my_dict['data'] = data
        jsonStr = dumps(my_dict)
        self.client.send(jsonStr.encode('utf-8'))
        self.client.close()


def init_socket_async():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind((localIp, 6789))
    server.listen(512)
    print('服务器启动监听...')
    while True:
        client, addr = server.accept()
        FileTransHandler(client).start()


class HttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        response = {'code': 200, 'msg': 'success'}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(dumps(response), 'utf-8'))


def init_http_server():
    server_address = ('localhost', 8000)
    httpd = socketserver.TCPServer(server_address, HttpHandler)
    print('服务器启动...')
    httpd.serve_forever()


if __name__ == '__main__':
    init_http_server()
