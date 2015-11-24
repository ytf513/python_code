#!/usr/bin/env python
#-*-  coding=utf-8 -*-

'regular expression test'

__author__="Alex Yean"
__date__="2015-11-9"

import re

s=raw_input("please input tel number:")
r_match=re.match(r'^\d{3}\-\d{3,8}',s)
if r_match:
    print "match ok"
else:
    print "match false"

print re.split(r"\s+","a b   c")

# compile
re_tel=re.compile(r"^(\d{3})\-(\d{3,8})$")
print re_tel.match("021-222222").groups()
