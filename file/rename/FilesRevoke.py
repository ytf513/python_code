#coding=gbk
#2013-12-12
#�ļ��ջ�
#��ĳ��Ŀ¼����Ŀ¼������Ŀ¼�ļ�ȫ���Ƶ���Ŀ¼�£���1������ļ����ظ����򲻴�����2�����Ŀ¼Ϊ�գ���ɾ��Ŀ¼

import os

#�����Ŀ¼��������input��input�����Ĭ��ΪPython���ʽ�����Ҫ��Ϊ�ַ���������������
destDir=raw_input("please input or paste the directory(���������ճ��Ŀ¼):")

for root,dirs,files in os.walk(destDir):
    print "[{0}]����{1}���ļ���{2}��Ŀ¼!".format(root,len(files),len(dirs))
    #��ǰĿ¼��������
    if root==destDir:
        continue
    #�ļ�Ϊ����ɾ��Ŀ¼
    if len(files)==0:
        print "[%s]Ŀ¼Ϊ�գ�����ɾ��!" % root
        os.rmdir(root)
        continue
    for x in files:
        if os.path.isfile(os.path.join(destDir,x)):
            print "[%s]�ļ��Ѿ����ڣ���������" % os.path.join(destDir,x)
        else:
            os.renames(os.path.join(root,x),os.path.join(destDir,x))
        
        
