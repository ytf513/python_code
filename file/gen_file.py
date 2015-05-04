#*-*coding:utf-8 *-*
'''
Created on 2012-6-14

@author: bitter_tea
注意红色这一行的描述，如果你seek到很长的位置去但是没有写入内容，那么这个文件是不会被延长(增大), 中间没有写数据的地方相当于只是占位，没有IO写，所以会很快。
     使用这个方法几秒钟就可以生成上百G的文件，非常好用。
'''
def gen_file(path,size):
    #首先以路径path新建一个文件，并设置模式为写
    file = open(path,'w')
    #根据文件大小，偏移文件读取位置 
    file.seek(1024*1024*size)#姑且以GB为单位吧
    #然后在当前位置写入任何内容，必须要写入，不然文件不会那么大哦
    file.write('\x00')
    file.close()
    
    
gen_file('test.dat',1)
