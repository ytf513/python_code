#����list.txt�ļ����ݵ�list2.txt
#�����ļ�֮ǰ�ȴ򿪣�д���ļ�֮ǰҲ���ȴ�

with open("list.txt",'rb') as file1:
    temp=file1.read(10)
    while(temp):
        print temp
        temp=file1.read(10)
    
