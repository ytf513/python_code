#login in xiami
#coding=utf-8
import urllib2
import urllib

def main():
	posturl = "http://www.xiami.com/member/login"
	data = {'email':"ytf513@gmail.com",'password':'Alex@google','autologin':'1','submit':"登 录",'type':''}
	post_data=urllib.urlencode(data)
	http_header={"User-Agent":"chrome"}
	http_request=urllib2.Request(posturl,post_data,http_header)
	print type(http_request)
	http_response=urllib2.urlopen(http_request)
	print http_response.info()
	with open("files/xiaomi.html",'wb') as f:
		f.write(http_response.read())

if __name__ == '__main__':
	main()

