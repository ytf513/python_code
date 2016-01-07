#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'负责启动wsgi服务器，加载application函数'

#从wsgiref中导入模块，wsgiref是一个wsgi的服务器模块，属于参考实现
from wsgiref.simple_server import make_server
from wsgi_hello import application

#创建一个服务器,处理函数是application
httpd=make_server("",8000,application)
print "Serving HTTP on port 8000...."

#开始监听http请求
httpd.serve_forever()
