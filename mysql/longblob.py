#!/usr/bin/python
#-*- coding: UTF-8 -*-
  
import MySQLdb as mysql
import sys
try:
    #��ȡͼƬ�ļ�
    fp = open("./test.jpg")
    img = fp.read()
    fp.close()
except IOError,e:
    print "Error %d %s" % (e.args[0],e.args[1])
    sys.exit(1)
try:
    #mysql����
    conn = mysql.connect(host='localhost',user='root',passwd='123456',db='test')
    cursor = conn.cursor()
    #ע��ʹ��Binary()������ָ���洢���Ƕ�����
    cursor.execute("INSERT INTO images SET data='%s'" % mysql.Binary(img))
    #������ݿ�û�������Զ��ύ������Ҫ�ύһ��
    conn.commit()
    cursor.close()
    #�ر����ݿ�����
    conn.close()
except mysql.Error,e:
    print "Error %d %s" % (e.args[0],e.args[1])
    sys.exit(1)