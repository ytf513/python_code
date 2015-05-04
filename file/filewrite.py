#拷贝list.txt文件内容到list2.txt
#读入文件之前先打开，写入文件之前也是先打开
a=[]
for i in range(1,5):
    a.append("This is line %s" % i)
astr="\n".join(a)

with open("list.txt","w") as file2:
    file2.write(astr)
    
