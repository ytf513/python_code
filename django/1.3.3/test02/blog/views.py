# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
def index(req):
	user={'name':'tom','age':23,'sex':'male'}
	#user=Person('tom',33,'male')
	book_list=['python','java','php','web']

	return render_to_response('index.html',{'title':'my page','book_list':book_list,'user':user})