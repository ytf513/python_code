#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'hashlib'

__all__=("Alex Yean","2015-11-09")

import hashlib
md5=hashlib.md5()
md5.update("How to use md5 in python hashlib")
print md5.hexdigest()
print hashlib.md5("dd").hexdigest()
