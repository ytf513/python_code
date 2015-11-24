#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'A '

__author__="Alex Yean"
__date__="2015-11-05"

#多进程中同一变量各自有一份拷贝存在与每个进程中，互不影响，但是多线程却是共享变量。

import time, threading
from multiprocessing import Process

# 假定这是你的银行存款:
balance = 0

def run_thread(n):
    a=0
    print "a id %s,current thread name is %s" % (id(a),threading.current_thread().name)  

#t2 = threading.Thread(target=run_thread, args=(8,))
#t2 = threading.Thread(target=run_thread, args=(8,))
p1 = Process(target=run_thread, args=(5,))
p2 = Process(target=run_thread, args=(8,))
#t1.start()
#t2.start()
p2.start()
p1.start()
#t1.join()
p1.join()
p2.join()
#t2.join()
print balance
