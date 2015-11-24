#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'进程间通信，用queque或pipes'

__author__="alex Yean"
__date__="2015-11-04"

import os,time,random
from multiprocessing import Process,Queue 

# write process code
def write(q):
    for value in ['A',"b","c"]:
        print "Put %s to queue,q id %s..." % (value,id(q))
        q.put(value)
        #q.append(value)
        time.sleep(random.random())

def read(q):
    while True:
        value=q.get(True)
        print 'Get %s from queue,q id %s...' % (value,id(q))
         

if __name__=='__main__':
    q=Queue()
    #q=[1,2,3]
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
