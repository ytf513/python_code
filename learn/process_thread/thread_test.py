#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'A multi thread Test'

__author__="Alex Yean"
__date__="2015-11-05"

#python提供了两个模块thread和threading，threading是对thread的封装。

import time,threading

def loop():
    print "thread %s is running..." % threading.current_thread().name
    n=0
    while n<5:
        n=n+1
        print 'thread %s >>> %s ' % (threading.current_thread().name,n)
        time.sleep(1)
    print  "thread %s ended." % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t=threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
print "thread %s ended." % threading.current_thread().name
