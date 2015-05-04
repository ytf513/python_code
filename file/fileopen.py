#coding=utf8
#方法1
with open("hashlib_test.py","rb") as f:
    line=f.readline()
    while(line):
        #print line
        line=f.readline()

#最好的读大文件的方法,stackoverflow中有人推荐
with open("hashlib_test.py","rb") as f:
    for line in f:
        print lineW




        
