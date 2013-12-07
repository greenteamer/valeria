# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from blog.views import PostList, PostDetail


urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='list'),
    url(r'^(?P<slug>[-_\w]+)/$', PostDetail.as_view(), name='detail'),
)
