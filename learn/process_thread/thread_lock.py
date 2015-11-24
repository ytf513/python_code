#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'A multi thread lock'

__author__="Alex Yean"
__date__="2015-11-05"

#多进程中同一变量各自有一份拷贝存在与每个进程中，互不影响，但是多线程却是共享变量。

import time, threading

# 假定这是你的银行存款:
balance = 0
lock=threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        #change_it(n)
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
