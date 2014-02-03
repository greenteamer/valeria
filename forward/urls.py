# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forward.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('main.urls')),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^portfolio/', include('portfolio.urls', namespace="folio")),
    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^flatblocks/', include("flatblocks.urls")),

    # хоп хей лалалалей

    #ok
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
