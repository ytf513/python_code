#coding=utf8
#map函数
#假设有一个数列，如何把每个元素都翻倍；如何求和两个数列

list_1=[1,2,3,4,5,6]
list_2=[1,3,5,7,9,11]

list_12=[i*2 for i in list_1]
print list_12

list_122=map(lambda i:i*2,list_1)
print list_122

list_22=map(None,list_1,list_2)
print list_22

list_221=map(lambda x,y:x+y,list_1,list_2)
print list_221

