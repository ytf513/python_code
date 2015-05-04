from django.conf.urls.defaults import patterns, include, url
#from blog.views import index
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'test01.views.home', name='home'),
    # url(r'^test01/', include('test01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^blog/index/$','blog.views.index') #o
	#url(r'^blog/index/$',index) #ok
    #url(r'^blog/index/\d{2}/$','index') #ok
    url(r'^blog/index/$','index'), #ok
    #url(r'^blog/index/(\d{2})/$','index'), #ok
)
