#!usr/bin/python
# -*- coding: UTF-8 -*-

# @author yintianfeng;@date:2017-11-10;@desc:rewrite the function

import smtplib # load smtp module
from email.header import Header
from email.mime.text import MIMEText

my_sender='plm@sieyuan.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_sender_show=u'PLM账户<plm@sieyuan.com>' #发件人邮箱账号，为了后面易于维护，所以写成了变量
server=smtplib.SMTP("10.10.2.8",25)  #发件人邮箱中的SMTP服务器，端口是25
server.login(my_sender,"plm@sieyuan")    #括号中对应的是发件人邮箱账号、邮箱密码

def send_mail(Send_from,Send_to,subject,body):
     try:
          msg=MIMEText('填写邮件内容','plain','utf-8')
          msg['From']=Send_from
          msg['To']=",".join(Send_to)
          msg['Subject']=Header(subject,'utf-8') #主题，通过Header编码
          server.sendmail(Send_from,Send_to,msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
          #如果try中的语句没有执行，则会执行下面的ret=False
          ret=True
     except Exception,e:
          print e
          ret=False
     return ret
	
send_mail(my_sender_show,["ytf.20822@sieyuan.com","20822"],"这是一封测试邮件","这是一封测试邮件")
#send_mail(my_sender_show,["ytf.20822@sieyuan.com","203478"],"这是一封测试邮件","这是一封测试邮件")

server.quit()   #这句是关闭连接的意思
