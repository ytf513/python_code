#����list.txt�ļ����ݵ�list2.txt
#�����ļ�֮ǰ�ȴ򿪣�д���ļ�֮ǰҲ���ȴ�
a=[]
for i in range(1,5):
    a.append("This is line %s" % i)
astr="\n".join(a)

with open("list.txt","w") as file2:
    file2.write(astr)
    
