#repeat execute the command
import time,os,sys
def main(cmd,inc=60):
	while True:
		os.system(cmd)
		time.sleep(inc)

if __name__=='__main__':
	numargs=len(sys.argv)-1
	print numargs
	if numargs<1 or numargs>2:
		print "usage:" + sys.argv[0]+ " command [seconds_delay]"
		sys.exit(1)
	cmd=sys.argv[1]
	if numargs==1:
		print sys.argv[1]
		main(cmd)
	else:
		print sys.argv[1],sys.argv[2]
		inc=int(sys.argv[2])
		main(cmd,inc)
