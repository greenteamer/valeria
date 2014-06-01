# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forward.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    url(r'^', include('main.urls')),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^portfolio/', include('portfolio.urls', namespace="folio")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^flatblocks/', include("flatblocks.urls")),

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += staticfiles_urlpatterns()
