#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 该代码发送邮件没有主题

import smtplib  
  
#fromaddr = 'plm@sieyuan.com'
fromaddr = 'plm@sieyuan.com'  
toaddrs  = 'ytf.20822@sieyuan.com'
#toaddrs  = 'ytf.20822@sieyuan.com'  
msg = 'There was New Test　Email吉萨'  
  
  
# Credentials (if needed)  
#username = 'ytf513'  
#password = 'jzY@473225'
username = 'plm@sieyuan.com'
password = 'plm@sieyuan'
#= 'Alex@473225'
  
# The actual mail send  
server = smtplib.SMTP('10.10.2.8')
#server = smtplib.SMTP('210.13.73.251')
#server = smtplib.SMTP('smtp.163.com:994')
#server.starttls()
server.login(username,password)
#server.login("","") 
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()  
