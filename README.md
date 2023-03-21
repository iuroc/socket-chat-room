# Socket 实现的聊天室

## 项目信息

- 作者：欧阳鹏
- 主页：https://apee.top
- 开发日期：2023 年 3 月 22 日
- 项目地址：https://github.com/oyps/socket-chat-room

## 安装使用

- Windows：下载 [`client.exe`](https://github.com/oyps/socket-chat-room/raw/master/dist/client.exe)，打开运行即可

## 服务端部署流程

1. 进入服务器某个目录
2. 将 `server.py` 上传到该目录
3. 运行 `python server.py`

## 模拟界面

```
请输入昵称：鹏优创社区
--------------------
大家好
>> 鹏优创社区：大家好
>> 昵称 A：大家好
>> 昵称 B：你好
```

## 数据结构

- 由客户端发给服务端的文本消息
    ```json
    {
        "message": "文本消息",
        "nick_name": "用户昵称",
        "type": "message"
    }
    ```