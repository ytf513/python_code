#listdir.py
import os  
# �ݹ����ָ����Ŀ¼  
# level -- �ݹ�Ĳ�������������������ƴ�ӡ������  
# path  == ������ʼ����·��  
def listyoudir(level, path):  
    for i in os.listdir(path):  
        print ('  '*(level+1) + i )
        with open(r"E:\Python\test\CodetestDir.txt",mode='a',encoding="utf-8") as f:
            f.write('  '*(level+1) + i +"\n")
        if os.path.isdir(path + '\\' + i):  
            listyoudir(level+1, path + '\\' + i)  
          
#���Դ���  
rootpath = os.path.abspath(r'd:\sieyuan')  
#print (rootpath)  
listyoudir(0, rootpath)

