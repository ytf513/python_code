#listdir.py
import os  
# 递归遍历指定的目录  
# level -- 递归的层数，用这个参数来控制打印的缩进  
# path  == 遍历起始绝对路径  
def listyoudir(level, path):  
    for i in os.listdir(path):  
        print ('  '*(level+1) + i )
        with open(r"E:\Python\test\CodetestDir.txt",mode='a',encoding="utf-8") as f:
            f.write('  '*(level+1) + i +"\n")
        if os.path.isdir(path + '\\' + i):  
            listyoudir(level+1, path + '\\' + i)  
          
#测试代码  
rootpath = os.path.abspath(r'd:\sieyuan')  
#print (rootpath)  
listyoudir(0, rootpath)

