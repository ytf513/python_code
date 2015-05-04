#coding=utf8
#md5 file content
import hashlib

def getFileMd5(fileName):
	with open(fileName) as ff:
		md5=hashlib.md5()
		for line in ff:
			md5.update(line)
	return md5.hexdigest()

print getFileMd5("testhash1.txt")
