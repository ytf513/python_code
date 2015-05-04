import socket
import time
 
def check(host,port):
    s = None
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except :
            s = None
            continue
        try:
            s.settimeout(2)
            s.connect(sa)
        except :
            s.close()
            s = None
            continue
        break
    if s is None:
        return 0
    s.close()
    return 1
 
 
def tester():
    checklist = [
        '10.10.2.6:1352',
        '10.10.2.7:1352',
        '10.10.2.8:1352',
        '10.10.2.9:1352',
        '10.10.2.10:1352',
        '10.10.2.12:1352',
        '192.168.1.1:1352',
        '192.168.1.4:1352',
        '10.10.4.12:1352',
        '121.42.41.146:1352'
        ]
 
    for checkitem in checklist:
        host, port = checkitem.split(':')
        if check(host, port):
            print ('%s\tis ok'%checkitem)
        else:
            print ('cannot connect to %s'%checkitem)
 
if __name__ == '__main__':
    tester()
    time.sleep(5)
