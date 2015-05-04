#details to see tools/webchecker/websucker.py
#usage:python+wget.py+url
import sys,urllib
def reporthook(*a):print a
for url in sys.argv[1:]:
	i=url.rfind('/')
	filetemp=url[i+1:]
	print url,"->",filetemp
	urllib.urlretrieve(url,filetemp,reporthook)