#!/usr/bin/env python
#-*- encoding=utf-8  -*-

__author__="Alex Yean"
__date__="2015-20-24"

'python调试'

#第一种简单粗暴得方式是print
#第二种是断言，凡是用print的地方都可以用断言

print "断言的使用方法："
def foo(s):
    n=int(s)
    assert n!=0,'n is zero!' # assert表达式n!=0应该是true,否则，后面的代码就会抛错
    return 10/n

#foo('0')

#第三种方法是logging
import logging
import os
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
s='0'
n=int(s)
logging.info('n=%d' % n)
print 10/n
print "also continue!"

#第四种，pdb

# logging的方式是终极武器
