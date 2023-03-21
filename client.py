import socket
import threading
import json

socket_client = socket.socket()  # 客户端 socket
host = 'docker.apee.top'  # 服务器主机名
port = 3003  # 服务端端口
local_host = socket.gethostname()  # 本地主机名
socket_client.connect((host, port))  # 连接到服务端
nick_name = input('请输入昵称：')
print('-' * 30)
data_default = {'type': 'message', 'nick_name': nick_name}  # 待发送消息数据
lock = threading.Lock()  # 创建锁


def send_message():
    '''发送消息'''
    while True:
        message_text = input()
        data_default['message'] = message_text
        data = json.dumps(data_default).encode()
        lock.acquire()
        socket_client.send(data)
        lock.release()


def receive_message():
    '''接收消息'''
    while True:
        data = socket_client.recv(1024).decode()
        lock.acquire()
        print(data)
        lock.release()


threading.Thread(target=send_message).start()
threading.Thread(target=receive_message).start()
