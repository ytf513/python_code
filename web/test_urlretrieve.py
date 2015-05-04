import urllib
def reportbook(a,b,c):
	#print a
	#print b
	#print c
	print "%.2f%%" % (100*a*b/c)

urllib.urlretrieve("http://www.python.org","files/baidu.html",reportbook)