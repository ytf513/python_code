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
    i=0
    checklist = [
	'symail:10.10.2.6:1352',
	'syapp:10.10.2.7:1352',
	'shr:10.10.2.8:1352',
	'shqn:10.10.2.9:1352',
	'syst2:10.10.2.12:1352',
	'sy:192.168.1.1:1352',
	'sy3:192.168.1.4:1352',
	'syoa:10.10.4.12:1352',
	'sycloud:121.42.41.146:1352',
	'bjqn:124.65.133.122:1352',
	'rgmail:61.177.200.186:1352'
	]

    telenet_result_list=[]
    for checkitem in checklist:
        i=i+1
        #print i
        shortname, host, port = checkitem.split(':')
        if check(host, port):
            telenet_result='%2s %15s %8s is ok.' % (i,host,shortname)
        else:
            telenet_result = '%2s %15s %8s is not ok,can\'t be connected!' % (i, host, shortname)
        print telenet_result
        telenet_result_list.append(telenet_result)
    return telenet_result_list
# 
# 
if __name__ == '__main__':
    with open("telnet_result.txt",'w') as f:
        f.write("At %s" % time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
        f.write("\n")
        f.write("\n".join(tester()))
    time.sleep(5)
