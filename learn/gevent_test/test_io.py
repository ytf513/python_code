#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'实现自动切换'

from gevent import monkey #;monkey.patch_all()
import gevent
import urllib2

def f(url):
    print "GET:%s" % url
    resp=urllib2.urlopen(url)
    data=resp.read()
    print "%d bytes received from %s." % (len(data),url)

gevent.joinall([
    gevent.spawn(f,"http://10.10.2.7"),
    gevent.spawn(f,"https://www.python.org"),
    gevent.spawn(f,"https://www.baidu.com"),
])
