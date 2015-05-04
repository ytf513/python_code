#coding=gbk
#2013-12-12
#文件收回
#把某个目录的子目录及以下目录文件全部移到该目录下，（1）如果文件名重复，则不处理；（2）如果目录为空，则删除目录

import os

#输入的目录，不能用input，input输入的默认为Python表达式，如果要变为字符串必须输入引号
destDir=raw_input("please input or paste the directory(请输入或者粘贴目录):")

for root,dirs,files in os.walk(destDir):
    print "[{0}]包括{1}个文件，{2}个目录!".format(root,len(files),len(dirs))
    #当前目录不做处理
    if root==destDir:
        continue
    #文件为空则删除目录
    if len(files)==0:
        print "[%s]目录为空，将被删除!" % root
        os.rmdir(root)
        continue
    for x in files:
        if os.path.isfile(os.path.join(destDir,x)):
            print "[%s]文件已经存在，不做处理！" % os.path.join(destDir,x)
        else:
            os.renames(os.path.join(root,x),os.path.join(destDir,x))
        
        
