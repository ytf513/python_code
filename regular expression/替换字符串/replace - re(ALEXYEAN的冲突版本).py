
#"2014-06-11 15:00:11 	ɾ�� sy2/siyuan"�������ַ�����ֻ��ȡ��sy2/siyuan��
import re
#a="2014-06-11 15:00:11 	ɾ�� sy2/siyuan"
#res=re.findall(r"ɾ�� (.*)/siyuan",a)
#help(res)
#print " ".join(res)
with open("a.txt") as f:
    a=f.readlines()
    for x in a:
        res=re.findall(r"ɾ�� (.*)/siyuan",x)
        print " ".join(res)
