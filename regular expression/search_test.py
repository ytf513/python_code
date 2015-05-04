#coding=utf8
#search:查找内容,将字符串的所有字符与正则表达式匹配，只找到第一个匹配的内容；findall是返回元组序列  
import re
searchStr="You are deleted yintianfeng@gis.com"
rx=r"deleted (.*)@gis\.(.*)$"
searchResult=re.search(rx,searchStr)
#group=group(0),group(1)=第一个返回的元素
print type(searchResult)
print searchResult.group(1),type(searchResult.group(1))
print searchResult.group(2)

#findall返回元组列表
searchResult1=re.findall(rx,searchStr)
print searchResult1
for x in searchResult1:
    print "-".join(x)

