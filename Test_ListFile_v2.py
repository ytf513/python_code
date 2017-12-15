# -*-  coding:utf-8 -*-
"""
@Author       : "Alex Yean"    
@Create Date  : "2017-12-15"
@Email        : "ytf513@foxmail.com"
@Description  : 
	
"""
import os
path=u"E:/weiyun/Java/" # r

#os.path.listdir方法
def get_FileName(root,level=1):
	""" 格式如下
	E:\TEST 
	│--A 
	│  │--A-A 
	│  │  │--A-A-A.txt 
	│  │--A-B.txt 
	│  │--A-C 
	│  │  │--A-B-A.txt 
	│  │--A-D.txt 
	│--B.txt 
	"""
	if level == 1: print root
	for file_name in os.listdir(root):
		path = os.path.join(root, file_name)
		print " |  " * (level-1) +" | -- %s" % file_name
		if os.path.isdir(path):
			get_FileName(path,level+1)

get_FileName(path)
