# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from portfolio.views import *


urlpatterns = patterns('',

    url(r'^$', FolioView.as_view(), name='folio_list'),
    url(r'^(?P<slug>[-_\w]+)/$', FolioDetail.as_view(), name='folio_detail'),
    # url(r'^(?P<slug>[-_\w]+)/$', 'portfolio.views.portfolio'),

)
