#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'Process and Thread usage'

__author__="Alex Yean"
__date__="2015-10-13"

print "multiprocessing多进程：Unix/Linux 提供了fork()系统调用,windows没有提供，所以无法使用fork"

import os
print "Process (%s) start..." % os.getpid()
pid=os.fork()
if pid==0:
    print "I am child process %s and my parent process is %s" % (os.getpid(),os.getppid())
else:
    print "I (%s) just created a child process (%s)." % (os.getpid(),pid)


