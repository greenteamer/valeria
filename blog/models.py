# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Post(models.Model):
    name = models.CharField(verbose_name=(u'Название статьи'), max_length=100)
    slug = AutoSlugField(editable=True, default='default', verbose_name=(u'ссылка'))
    title = models.CharField(verbose_name=(u'title'), max_length=60)
    description = models.CharField(verbose_name=(u'description'), max_length=160)
    keywords = models.CharField(verbose_name=(u'keywords'), max_length=60)
    date = models.DateTimeField(verbose_name=(u'Дата создания'), auto_now_add=True, null=True)
    text = RichTextField()
    image = models.ImageField(verbose_name=(u'Изображение'), upload_to='blog')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/%s' % self.slug

    class Meta:
        verbose_name = (u'Статья')
        verbose_name_plural = (u'Статьи')
