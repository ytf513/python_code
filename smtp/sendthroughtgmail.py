import smtplib  
  
fromaddr = 'ytf513@gmail.com'
fromaddr = 'ytf.20822@sieyuan.com'  
toaddrs  = 'ytf5131@gmail.com'  
msg = 'There was New Test¡¡Email'  
  
  
# Credentials (if needed)  
#username = 'ytf513'  
#password = 'jzY@473225'
username = 'ytf513'
password = 'jzY@473225'
#= 'Alex@473225'
  
# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')
#server = smtplib.SMTP('smtp.163.com:994')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()  
