#!/usr/bin/env python
#-*- encoding=utf-8  -*-

__all__={"Alex Yean","2015-11-13"}

# 导入socket库:
import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
print s.recv(1024)
# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

# 关闭连接:
s.close()

header,html=data.split('\r\n\r\n',1)
print header
with open('sina.html','wb') as f:
    f.write(html)
with open('sina.txt','wb') as f:
    f.write(data)
