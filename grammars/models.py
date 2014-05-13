# -*- coding: utf-8 -*-
from django.db import models

class Gram(models.Model):
    name = models.CharField(max_length=255, verbose_name=(u'Имя'))
    date = models.DateTimeField(verbose_name=(u'Дата'), auto_now_add=True)
    alt = models.CharField(verbose_name=(u'Альт текст в картинку'), max_length=255)
    image = models.ImageField(verbose_name=(u'Бланодарственное письмо'), upload_to='gram', null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = (u'Грамоты')
        verbose_name_plural = (u'Грамота')
