#encoding=utf8
#函数式编程，python提供部分支持，因为python允许使用变量
#高阶函数：变量可以指向函数，函数可以作为另一个函数的参数
def add(x,y,f):
	return f(x)+f(y)

print "abs(-6)+abs(2):",add(2,-6,abs)

print "*"*40

print "Map/Reduce函数测试"
# reduce的功能是：首先接收两个参数，然后把计算结果继续和序列的下一个函数做累积计算
alist=['adam', 'LISA', 'barT']
print map(lambda x:x.capitalize(),alist)
print reduce(lambda x,y:x*y,[1,2,3,4])

print 'filter()过滤函数，根据第一个参数的True、False过滤列表'
from math import sqrt
def sushu(n):
	i=2
	while i<sqrt(n):
		if n%i==0:
			return False
		i=i+1
	return True

print filter(sushu,range(1,1001))

print "*"*40

# 函数作为返回值：闭包
def calc_sum(*args):
	def sum():
		total=0
		for x in args:
			total=total+x
		return total
	return sum

f=calc_sum(1,2,3,4)
print f
print f()

# 利用lambda关键字可以生成匿名函数，python对匿名函数的支持有限

print "*"*40
print "装饰器:在代码运行期间动态增加功能的方式为，装饰器Decorator"
# 接受一个函数作为参数，并返回一个函数
def log(func):
	def wrapper(*args,**kw):
		print 'call %s' % func.__name__
		return func(*args,**kw)
	return wrapper

@log # 相当于执行了now=log(now)
def now():
	print "2015-10-21"

now()
print log(now)()
print now.__name__
#装饰器之后的函数已不是原来的函数，为了避免这样的副作用，可以在函数之前加上functools.wraps

print "*"*40
print "偏函数,用functools.partical模块实现偏函数，可以固定某个参数"
