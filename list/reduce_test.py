#coding=utf8
#test reduce

a=[1,2,3,4,5]

print reduce(lambda x,y:x+y,a)

alist=filter(lambda x:x%2==0,a)
print alist
