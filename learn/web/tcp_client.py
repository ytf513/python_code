#!/usr/bin/env python
# encoding=utf-8

__all__={"Alex Yean","2015-11-13"}

# 导入socket库:
import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1',9999))
print s.recv(1024)
for data in ["Alex","Amily","Sara"]:
    s.send(data)
    print s.recv(1014)
s.send("exit")
s.close()
