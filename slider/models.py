# -*- coding: utf-8 -*-
from django.db import models

class Slider(models.Model):
    image = models.ImageField(verbose_name=(u'Изображение'), upload_to='slider')
    name = models.CharField(verbose_name=(u'Заголовок') ,max_length=150, null=True)
    text = models.TextField(verbose_name=(u'Текст'), max_length=250, null=True)
    link = models.CharField(verbose_name=(u'Ссылка'), max_length=60, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = (u'Слайдер')
        verbose_name_plural = (u'Слайды')