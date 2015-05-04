#coding=utf8
#str.translate与re.sub有类似的功能,string.maketrans(frm,org)与str.translate#配合使用，产生table

import string
a="Good,ok#okay"
tranTable=string.maketrans(",#","--")

b=a.translate(tranTable,"")
print "The old:",a
print "The new:",b
