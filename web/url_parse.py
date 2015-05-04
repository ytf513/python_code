from urlparse import urlparse 
urlstr="http://www.zhihu.com/topic/dfadsf/ddd"
url=urlparse(urlstr)
print 'Protocol:',url.scheme
print 'Hostname:',url.hostname
print 'Port:',url.port
print 'Path:',url.path
print 'query:',url.query	#query parameters 

i=len(url.path)-1
while i>0:
	if url.path[i]=="/":
		break
	i=i-1

print 'filename:',url.path[i+1:len(url.path)]