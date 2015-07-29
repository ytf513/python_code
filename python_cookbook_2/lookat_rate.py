# coding:utf8
# Autor:Alex Yean
# Date:2015-07-22
# 监控货币之间的兑换比例

import httplib
import smtplib

# settings
thresholdRate=1.30
stmpserver='smtp.freebie.com'
fromaddr='foo@bar.com'
toaddrs='your@corp.com'
# settings Over

url='/index.aspx?cat_code=GIS'
conn=httplib.HTTPConnection('www.sieyuan.com')
conn.request('GET',url)
response=conn.getresponse()
data=response.read()
#print data
start=data.index("HGIS")
print start
line=data.index("<a>",start)
print line
