from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.post_list, name = 'post_list'),
		url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
		url(r'^post/new/$', views.post_new, name='post_new'),
		url(r'^login/$', views.login, name='login'),
		url(r'^logout/$', views.user_logout, name='logout'),
		url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name= 'add_comment_to_post'),
        url(r'^post/(?P<pk>[0-9]+)/comment/(?P<fuck>[0-9]+)/edit/$', views.comment_edit, name='comment_edit'),
        url(r'^post/(?P<pk>[0-9]+)/comment/(?P<fuck>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]
