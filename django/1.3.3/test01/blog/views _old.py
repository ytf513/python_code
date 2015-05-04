# Create your views here.
#from django.http import HttpResponse
#def index(req):
	#return HttpResponse('<h1>Hello welcome to Django!</h1>')

from django.shortcuts import render_to_response
class Person(object):
	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex

	def say(self):
		return "I'm "+self.name

def index(req,id):
	user={'name':'tom','age':23,'sex':'male'}
	book_list=['python','java','php','web']

	return render_to_response('index.html',{'title':'my page','book_list':book_list,'user':user,'id':id})
