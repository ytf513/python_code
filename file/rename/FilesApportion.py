#coding=gbk
#2013-12-12
#�ַ��ļ�������Ŀ¼
#��ָ��Ŀ¼�У������ļ�����ǰ׺���Ѹ�Ŀ¼��ǰ׺��ͬ���ļ���������Ӧǰ׺�������ļ��У���Щ�ļ���Ҳ���ڸ�Ŀ¼�£���
#(1)����ļ������Ȳ��㣬��������

import os

#�����Ŀ¼��������input��input�����Ĭ��ΪPython���ʽ�����Ҫ��Ϊ�ַ���������������
destDir=raw_input("please input or paste the directory(���������ճ��Ŀ¼):")
#���ĵ�ǰ����Ŀ¼������
os.chdir(destDir)
print "��ǰ����������Ŀ¼Ϊ��%s"  % os.getcwd()
#����ǰ׺λ���Ƕ���
suffixLen=int(raw_input("ǰ׺�ж���λ:"))

for fileTemp in os.listdir(destDir):
    fileTemp=fileTemp.decode("gbk")
    if os.path.isdir(fileTemp):
        #print "[%s]�Ǹ�Ŀ¼����������" % os.path.join(destDir,fileTemp)
        continue
    #�ļ���׺����������
    if len(os.path.splitext(fileTemp)[0])<suffixLen:
        print "[%s]�ļ���̫�̣���������" % os.path.join(destDir,fileTemp)
    else:
        #os.renames(fileTemp,"%s\\%s" % (fileTemp[0:suffixLen],fileTemp)) # ���ַ�ʽ������ƽ̨�л�
        os.renames(fileTemp,os.path.join(fileTemp[0:suffixLen],fileTemp))
