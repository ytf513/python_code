# -*-  coding:utf-8 -*-
"""
@Author       : "Alex Yean"    
@Create Date  : "2017-11-14"
@Email        : "ytf513@foxmail.com"
@Description  : 发送邮件代码 版本5
"""

import smtplib
from email.header import Header
from email.mime.text import MIMEText

my_sender="plm@sieyuan.com"
my_sender_alias=u"<PLM科>plm@sieyuan"
#获取SMTP Server
def get_smtp_server():
	try:
		smtp_server=smtplib.SMTP("10.10.2.8",25) #SMTP Connect
		smtp_server.login(my_sender,"plm@sieyuan") #Login in with user and password
		return smtp_server
	except Exception, e:
		print e
		return None

#定义一个全局变量，免得重复Connect Smtp Server，降低资源消耗
smtp_server=get_smtp_server();
#失败则终止程序
if smtp_server is  None:
	print "连接SMTP失败！"
	exit(0)

def send_mail(send_from, send_to, subject, body):
	"""定义一个发送邮件函数，方便发送邮件调用"""
	try:
		msg = MIMEText(body, "plain", "utf-8")
		msg["From"] =my_sender_alias
		msg["To"] = send_to
		msg["Subject"] = Header(subject, "utf-8")
		smtp_server.sendmail(send_from, send_to, msg.as_string())
		#smtp_server.sendmail(send_from, send_to,"") #msg参数不带时,对方收到的邮件没有主题等内容
		ret = True
	except Exception, e:
		print e
		ret = False
	return ret

#可以重复调用Send_Mail()
send_mail(my_sender,"120822","这是主题","这是正文")

#关闭SMTP
smtp_server.quit()










