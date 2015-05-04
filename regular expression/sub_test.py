#coding=utf8
#sub:替换字符串
import re
searchStr="You are deleted yintianfeng@gis.com"
rx=r"@gis\.(.*)$"
searchResult=re.sub(rx,"gis.org",searchStr)
print searchResult,type(searchResult)

searchStr="good,ok#okay@"
rc=re.compile(r"[,#@]")
searchResult=rc.sub("-",searchStr)
print searchResult

