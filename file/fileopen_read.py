#拷贝list.txt文件内容到list2.txt
#读入文件之前先打开，写入文件之前也是先打开

with open("list.txt",'rb') as file1:
    temp=file1.read()
    
with open("list2.txt","wb") as file2:
    file2.write(temp)
    
