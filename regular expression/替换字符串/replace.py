#coding=gbk
#"2014-06-11 15:00:11 	删除 sy2/siyuan"这样的字符串，只获取“sy2/siyuan”
a=[]
b=[]
ff=open("b.txt","w")
with open("a.txt") as f:
    a=f.readlines()
    for x in a:
        #print x
        #print x.find("删除")
        y=x[x.find("删除 "):]
        y=y[y.find(" ")+1:]
        ff.write(y)

ff.close()
