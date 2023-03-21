# socket 实现的聊天室

## 项目信息

- 作者：欧阳鹏
- 开发日期：2023 年 3 月 22 日
- 主页：https://apee.top

## 模拟界面

```
请输入用户名：欧阳鹏
┌─────────────────────┐
│ 欢迎来到 APEE 聊天室 │
├─────────────────────┤
│ IP: 123.21.111.212  │
└─────────────────────┘
昵称 A 加入
>> 昵称 A：大家好
>> 昵称 B：你好
昵称 C 离开
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

## 其他

```
┌─────────┬───┬───┬───┐
│ (index) │ 0 │ 1 │ 2 │
├─────────┼───┼───┼───┤
│    0    │ 1 │ 2 │ 3 │
│    1    │ 2 │ 2 │ 2 │
└─────────┴───┴───┴───┘
```