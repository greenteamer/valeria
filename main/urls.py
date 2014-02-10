# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from main.views import *
from portfolio.views import *


urlpatterns = patterns('',
    # url(r'^$', MainView.as_view(), name='main'),

    url(r'^$', 'main.views.mainpage'),
    url(r'^sozdanie-saitov/$', 'main.views.sozdanie'),
    url(r'^prodvijenie/$', 'main.views.prodvijenie'),
    url(r'^mobilnie-prilojeniya/$', MobileView.as_view(), name='mobile'),
    url(r'^kontakty/$', 'feedback.views.contact'),


    # url(r'^portfolio/$', FolioView.as_view(), name='folio'),


    # url(r'^prodvijenie/$', ProdvijenieView.as_view(), name='prodvijenie'),
)
