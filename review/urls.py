from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.post_list, name = 'post_list'),

    url(r'new/$', views.post_new, name = 'post_new'),

    url(r'^(?P<id>\d+)/$', views.post_detail, name = 'post_detail'),

    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name = 'post_edit'),

    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name = 'post_delete'),

    url(r'^comment/(?P<id>\d+)/edit/$', views.comment_edit, name = 'comment_edit'),

    url(r'^comment/(?P<id>\d+)/delete/$', views.comment_delete, name = 'comment_delete'),

    url(r'^(?P<keyword>[ㄱ-힣]+)$', views.tag_filter, name = 'tag_filter'),

    url(r'^(?P<id>\d+)/like/$', views.post_like, name = 'post_like'),

]