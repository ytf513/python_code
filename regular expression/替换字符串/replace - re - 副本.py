#coding=gbk
#"2014-06-11 15:00:11 	ɾ�� sy2/siyuan"�������ַ�����ֻ��ȡ��sy2/siyuan��
import re
a="2014-06-11 15:00:11 	ɾ�� �����sy2/siyuan"
res=re.findall(r"ɾ�� [\w\W]*/siyuan",a)
#help(res)
print type(res)
print " ".join(res)
