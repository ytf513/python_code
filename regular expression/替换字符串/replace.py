#coding=gbk
#"2014-06-11 15:00:11 	ɾ�� sy2/siyuan"�������ַ�����ֻ��ȡ��sy2/siyuan��
a=[]
b=[]
ff=open("b.txt","w")
with open("a.txt") as f:
    a=f.readlines()
    for x in a:
        #print x
        #print x.find("ɾ��")
        y=x[x.find("ɾ�� "):]
        y=y[y.find(" ")+1:]
        ff.write(y)

ff.close()
