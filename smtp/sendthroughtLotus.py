import smtplib  
  
#fromaddr = 'plm@sieyuan.com'
fromaddr = 'plm@sieyuan.com'  
toaddrs  = 'ytf513@foxmail.com'
#toaddrs  = 'ytf.20822@sieyuan.com'  
msg = 'There was New Test¡¡Email'  
  
  
# Credentials (if needed)  
#username = 'ytf513'  
#password = 'jzY@473225'
username = 'plm@sieyuan.com'
password = 'plm@sieyuan'
#= 'Alex@473225'
  
# The actual mail send  
server = smtplib.SMTP('10.10.2.7')
#server = smtplib.SMTP('smtp.163.com:994')
#server.starttls()
server.login(username,password)
#server.login("","") 
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()  
