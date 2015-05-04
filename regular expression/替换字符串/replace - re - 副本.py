#coding=gbk
#"2014-06-11 15:00:11 	删除 sy2/siyuan"这样的字符串，只获取“sy2/siyuan”
import re
a="2014-06-11 15:00:11 	删除 计算机sy2/siyuan"
res=re.findall(r"删除 [\w\W]*/siyuan",a)
#help(res)
print type(res)
print " ".join(res)
