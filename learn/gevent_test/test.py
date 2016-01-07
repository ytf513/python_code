#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'gevent 实现协程'

from gevent import monkey #;monkey.patch_socket()
import gevent

def f(n):
    for i in range(5):
        print gevent.getcurrent(),i
        gevent.sleep(0)

g1=gevent.spawn(f,5)
g2=gevent.spawn(f,5)
g3=gevent.spawn(f,5)
g1.join()
g2.join()
g3.join()
