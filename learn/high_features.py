#encoding=utf8
#python的高级特性

print "切片操作" #可以用循环等实现
alist=["apple",'amazone','goog','micro','ebay']
print alist
print "取前三个元素：",alist[0:3]
print "每两个取一个：",alist[::2]
print "反转：",alist[::-1]

print "*"*40

print "迭代：无论是否有下标，只要是可迭代对象，都可以迭代。"
adict={'apple':'APPL','google':'GooG','micro':"MIC"}
for x in adict:
	print x

print "*"*40

print "列表生成式"
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() if isinstance(s,str) else s for s in L]

print "*"*40

print "生成器"
print "创建生成器的方法有多种，一种简单的方法是把列表推导式的[]改为()"

