# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from main.views import ReviewDetailView

urlpatterns = patterns('',

    # url(r'^$', FolioView.as_view(), name='folio_list'),
    url(r'^(?P<slug>[-_\w]+)/$', ReviewDetailView.as_view(), name='review_detail'),
    # url(r'^(?P<slug>[-_\w]+)/$', 'portfolio.views.portfolio'),

)
