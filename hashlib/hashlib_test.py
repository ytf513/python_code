#coding=utf8
import hashlib
md5=hashlib.md5()#创建一个MD5加密对象
md5.update("Good is a handsome boy!")#加密后的结果（二进制）  
#print md5.digest()#加密后的结果（二进制）  
print md5.hexdigest() #加密后的结果，用十六进制字符串表示。
print "Block_size:",md5.block_size
print "digest_size:",md5.digest_size

#print hashlib.new("md5", "JGood is a handsome boy").hexdigest() #一句话MD5加密，并用十六进制显示
