#coding=utf-8
#递归的应用
def fib(n):
	print "n=",n
	if n>1:
		return n*fib(n-1)
	else:
		print "The end of the line"
		return 1