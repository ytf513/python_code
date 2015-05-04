#coding=gbk
with open("a.csv") as f:
	b=f.readlines()
res=[]	
for x in b:
    a=x.split()
    res.append(a)

print res

with open("b.txt","w") as f:
    for x in res:
        f.writelines(str(x))

    f.write('\n')
    f.write('2013') 
