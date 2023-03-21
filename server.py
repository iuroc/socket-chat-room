import socket
import threading
import json

socket_server = socket.socket()  # 服务端 socket
host = socket.gethostname()  # 主机名
port = 3003  # 端口
socket_server.bind((host, port))  # 绑定主机
socket_server.listen(30)  # 最大连接数
socket_client_list = []  # 客户端 socket 列表
lock = threading.Lock()  # 创建锁
print('Github: https://github.com/oyps/socket-chat-room')
print('Server is running...')


def client_online(socket_client: socket.socket):
    '''客户端上线'''

    def client_offline():
        '''客户端下线'''
        lock.acquire()  # 上锁
        socket_client_list.remove(socket_client)
        lock.release()  # 解锁

    # 客户端已连接，加入数组记录
    lock.acquire()  # 上锁
    socket_client_list.append(socket_client)
    lock.release()  # 解锁
    while True:
        try:
            data = socket_client.recv(1024)  # 等待客户端发送数据
        except:
            return client_offline()  # 客户端下线
        if not data:
            return client_offline()  # 客户端下线
        ####################
        lock.acquire()  # 上锁
        data_dict = json.loads(data)
        nick_name = data_dict['nick_name']
        message = data_dict['message']
        res_type = data_dict['type']
        if res_type == 'message':  # 由客户端发来的文本消息
            # 待发送的文本
            send_text: str = f'>> {nick_name}：{message}'
        else:
            send_text = ''
        for i in socket_client_list:  # 发送给每个客户端
            i.send(send_text.encode())
        ####################
        lock.release()  # 解锁


while True:
    # 等待客户端连接
    socket_client, address = socket_server.accept()
    # 开始对客户端的事件处理
    threading.Thread(target=client_online, args=(socket_client,)).start()
