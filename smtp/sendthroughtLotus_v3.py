#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 该代码发送邮件没有主题
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
my_sender='plm@sieyuan.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='ytf.20822@sieyuan.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
#from email.header import Header
#from = ("%s<outofmemory_cn@126.com>") % (Header('OutOfMemory.CN管理员','utf-8'))
def mail():
    ret=True
    try:
        msg=MIMEText(u'填写邮件内容','plain','utf-8')
        msg['From']=formataddr(["FOL科",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["小尹A",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=Header('主题','utf-8') #邮件的主题，也可以说是标题

        server=smtplib.SMTP("10.10.2.8",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"plm@sieyuan")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
	#如果try中的语句没有执行，则会执行下面的ret=False
    except Exception,e:
        print e
        ret=False
    return ret

ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed
