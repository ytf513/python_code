#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'wsgi处理函数，只能wsgi服务器来调用'

def application(environ,start_response):
    start_response('200 OK',[('Content-Type',"text/html")])
    #help(start_response)
    help(environ)
    return '<h1>Hello %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
