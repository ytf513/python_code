#coding=utf8
#match:只从字符串的开始与表达式匹配，匹配成功返回matchobject,否则返回None.该函数的功能在匹配字符串，而非查找
import re
searchStr="You are deleted yintianfeng@gis.com"
rx=r"You are deleted (.*)@gis\.(.*)ss"
searchResult=re.match(rx,searchStr)
#group=group(0),group(1)=第一个返回的元素
print type(searchResult)
if searchResult:
    print searchResult.group(0),type(searchResult.group(0))

