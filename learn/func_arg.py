#encoding=utf8
#默认参数必须指向不可变对象


##默认参数
print "默认参数"
def add_append(l=[]):
	l.append("app")
	return l

print add_append()
print add_append() #此时为['app','app'],在函数定义的时候，默认函数就被计算出来了,
		   #它指向变量[]，所以每次调用之后，变量内容就变了
print "*"*40

##可变参数
print "可变参数"
##就是传入的参数个数是不缺定的，可以是一个两个或者任意一个，0个
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1,2,3,4)
print calc(*[1,2,3,4]) # 可以通过在list或tuple前面加*把其当作可变参数传进去


print "*"*40

## 关键字参数
print "关键字参数"
## 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
	print "name=",name,"age=",age,kw

person('alex',30,address="aaa")
kw={"city":"beijing","job":"software engineer"}
person('alex',30,**kw)

## summary
## 可变参数可以直接传入func(1,2,3),也可以封装为tuple传入，func(*(1,2,3))
## 关键字参数可以直接传入func(a="3"),也可以封装dict后传入，func(**{a:"3"})


print "*"*40

# 递归函数
print "递归函数"
def fac(n):
	if n<1:
		return 0
	elif n==1:
		return 1
	else:
		return n*fac(n-1)
n=int(raw_input('please input number n:'))
print fac(n)
'''循环的表达方式
def fac(n):
...     total=1
...     while n>=1:
...             total=total*n
...             n=n-1
...     return total
'''

print "*"*40
print "尾递归优化" # python的解释器没有做尾调用的优化，所以即使为尾调用的方式，也是会有堆栈报错
def fac_r(n,total=1):
	if n<1:
		return 0
	if n==1:
		return total
	else:
		return fac_r(n-1,total*n)

print fac_r(n)
