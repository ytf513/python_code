#coding=gbk
#2013-12-12
#分发文件到各个目录
#在指定目录中，根据文件名的前缀，把该目录下前缀相同的文件放入以相应前缀命名的文件夹（这些文件夹也放于该目录下）中
#(1)如果文件名长度不足，不做处理

import os

#输入的目录，不能用input，input输入的默认为Python表达式，如果要变为字符串必须输入引号
destDir=raw_input("please input or paste the directory(请输入或者粘贴目录):")
#更改当前操作目录到这里
os.chdir(destDir)
print "当前正常操作的目录为：%s"  % os.getcwd()
#输入前缀位数是多少
suffixLen=int(raw_input("前缀有多少位:"))

for fileTemp in os.listdir(destDir):
    fileTemp=fileTemp.decode("gbk")
    if os.path.isdir(fileTemp):
        #print "[%s]是个目录，不做处理！" % os.path.join(destDir,fileTemp)
        continue
    #文件后缀不算作长度
    if len(os.path.splitext(fileTemp)[0])<suffixLen:
        print "[%s]文件名太短，不做处理！" % os.path.join(destDir,fileTemp)
    else:
        #os.renames(fileTemp,"%s\\%s" % (fileTemp[0:suffixLen],fileTemp)) # 这种方式不利于平台切换
        os.renames(fileTemp,os.path.join(fileTemp[0:suffixLen],fileTemp))
