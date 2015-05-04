# -*- coding: cp936 -*-
import urllib
a_url = 'http://www.sieyuan.com/ckfinder/userfiles/files/20120817_095738.pdf'
data = urllib.urlopen(a_url).read()
type(data)

with open(r'files/sieyuan.pdf', mode='w') as a_file: 
	a_file.write(data)
