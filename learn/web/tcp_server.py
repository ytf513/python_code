#!/usr/bin/env python
# encoding=utf-8

__all__={"Alex Yean","2015-11-13"}

# 导入socket库:
import socket
import threading,time
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print "waiting for connection...."

def tcplink(sock,addr):
    print "Accept new connection from %s:%s..." % addr
    sock.send("welcome!")
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=="exit" or not data:
            break
        sock.send("Hello,%s" % data)
    sock.close()
    print "Connction from %s:%s closed." % addr


while(True):
    sock,addr=s.accept()
    #创建新线程来处理TCP链接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
