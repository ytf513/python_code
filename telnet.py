import telnetlib
 
HOST = "10.10.2.9"
PORT = 1352
t = telnetlib.Telnet()
t.open(HOST,PORT)
