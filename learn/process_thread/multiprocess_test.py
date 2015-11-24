#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'Process and Thread usage'


print "Python提供了跨平台的多进程支持，multiprocessing类提供"
import os
import time
from multiprocessing import Process

#define subprocess function
def run_proc(name):
    print "Run child process %s (%s)" % (name,os.getpid())
    time.sleep(20)

if __name__=="__main__":
    print "Parent process %s." % os.getpid()
    p=Process(target=run_proc,args=('test',))
    print "Process %s  will start." % (os.getpid())
    p.start()
    time.sleep(4)
    p.terminate()
    print "Process %s end." % (os.getpid())

