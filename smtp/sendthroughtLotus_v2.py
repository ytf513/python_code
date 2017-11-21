#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import os
import commands
from email.mime.text import MIMEText
from email.header import Header
def send(a,b):
    user = 'plm@sieyuan.com'
    from_addr = 'plm@sieyuan.com'
    password = 'plm@sieyuan'
    smtp_server = '10.10.2.8'
    to_addr = b
    print "##############"+to_addr
    #以下语句保证了发件人可以显示出来
    msg['To'] = Header(to_addr, 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(user, password)
    print '**************'+to_addr
    server.sendmail(from_addr, to_addr, a.as_string())
    server.close()
if __name__ == '__main__':
            msg = MIMEText('内容文字内容文字', 'plain', 'utf-8')
            msg['Subject'] =Header('我是标题', 'utf-8')
            q=send(msg,"小尹<ytf.20822@sieyuan.com>")
