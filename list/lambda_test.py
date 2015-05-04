#coding=utf8
#lambda 一行第一函数，filter,sort等内嵌函数比较适合用lambda

fn=lambda x,y:x+y #不含输入参数

def fn1(x,y):
    return x+y

print fn(3,3)
print fn1(4,3)

