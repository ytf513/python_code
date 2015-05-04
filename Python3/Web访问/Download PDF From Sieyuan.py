import urllib.request
a_url = 'http://www.sieyuan.com/ckfinder/userfiles/files/20120817_095738.pdf'
data = urllib.request.urlopen(a_url).read()

with open(r'd:\1.pdf', mode='wb') as a_file: 
	a_file.write(data)