#拷贝list.txt文件内容到list2.txt
#读入文件之前先打开，写入文件之前也是先打开

with open("list.txt",'rb') as file1:
    temp=file1.read(10)
    while(temp):
        print temp
        temp=file1.read(10)
    
