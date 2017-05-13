from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/',include(admin.site.urls)),
    	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'', include('blog.urls')),
)
