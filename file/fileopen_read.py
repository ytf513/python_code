#����list.txt�ļ����ݵ�list2.txt
#�����ļ�֮ǰ�ȴ򿪣�д���ļ�֮ǰҲ���ȴ�

with open("list.txt",'rb') as file1:
    temp=file1.read()
    
with open("list2.txt","wb") as file2:
    file2.write(temp)
    
