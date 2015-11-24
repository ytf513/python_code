#!/usr/bin/env python
#-*- encoding=utf-8  -*-

__author__="alex yean"
__date__="2015-11-04"

'io 测试,包括序列化'

try:
    import cPickle as pickle
except IOError,e:
    import pickle

d=dict(name="bob",age=10,score=88)
with open('pickle.bak','w') as f:
    #i=pickle.dumps(d) #dumps把任意对象序列化为一个str，然后可以写入文件
    #f.write(i)
    pickle.dump(d,f) # dump可以取代上两行代码

with open('pickle.bak','r') as f:
    o=pickle.load(f)
    print o

print "*"*40

import json
with open('json.bak','w') as f:
    json.dump(d,f)

with open('json.bak','r') as f:
    o=json.load(f)
    print o

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
#print(json.dumps(s)) 默认情况下class不是可序列化的对象
print(json.dumps(s, default=lambda obj: obj.__dict__))

with open('json2.bak','w') as f:
    json.dump(s,f,default=lambda obj: obj.__dict__)
