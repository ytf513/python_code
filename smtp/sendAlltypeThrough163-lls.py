#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
  
sender = 'ytf513@163.com'  
receiver = 'ytf.20822@sieyuan.com'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = 'ytf513'  
password = 'Alex@20822'  
  
# Create message container - the correct MIME type is multipart/alternative.  
msg = MIMEMultipart('alternative')  
msg['Subject'] = "Link"  
  
# Create the body of the message (a plain-text and an HTML version).  
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"  
html = """\ 
<html> 
  <head></head> 
  <body> 
    <p>Hi!<br> 
       How are you?<br> 
       Here is the <a href="http://www.python.org">link</a> you wanted. 
    </p> 
  </body> 
</html> 
"""  
  
# Record the MIME types of both parts - text/plain and text/html.  
part1 = MIMEText(text, 'plain')  
part2 = MIMEText(html, 'html')  
  
# Attach parts into message container.  
# According to RFC 2046, the last part of a multipart message, in this case  
# the HTML message, is best and preferred.  
msg.attach(part1)  
msg.attach(part2)  
#构造附件  
att = MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = 'attachment; filename="1.jpg"'  
msg.attach(att)  
     
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.starttls()  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  
