import urllib2
import time

def main():
    opener = urllib2.build_opener()
    while 1:
        request = urllib2.Request('http://xinhuanet.com/') 
        page = opener.open(request)
        print page.code
        print 'sleeping...'
        time.sleep(60)

if __name__ == '__main__':
    main()
