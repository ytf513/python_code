#coding=utf-8
#闭包
flist = []
 
for i in xrange(3):
    def func(x): return x * i
    flist.append(func)

print i

for f in flist:
    print f(2)
