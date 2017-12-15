# -*-  coding:utf-8 -*-
"""
@Author       : "Alex Yean"    
@Create Date  : "2017-12-15"
@Email        : "ytf513@foxmail.com"
@Description  : 
"""
import os
path=u"E:/weiyun/Java/" # r

#os.walk方法
for root,dirs,files in os.walk(path):
	for filename in files:
		print os.path.join(root,filename)
		#print os.access(root,os.R_OK|os.W_OK)
print "#"*40
#两段代码一样
#os.path.listdir方法
def get_FileName(root):
	for file_name in os.listdir(root):
		path = os.path.join(root, file_name)
		if os.path.isdir(path):
			get_FileName(path)
		else:
			print path

get_FileName(path)