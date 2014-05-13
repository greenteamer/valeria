# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class Review(models.Model):
    name = models.CharField(verbose_name=(u'Имя'), max_length=155)
    company = models.CharField(verbose_name=(u'Компания'), max_length=155, null=True)
    date = models.DateTimeField(verbose_name=(u'Дата'), auto_now_add=True)
    text = RichTextField()
    image = models.ImageField(verbose_name=(u'Фото'), upload_to='reviews', null=True)

    main_choice = models.CharField(
        max_length=7,
        verbose_name = (u'На главную'),
        choices=(
            ('notmain', 'нет'),
            ('main', 'да'),
        ),
        default='notmain'
    )

    def review_in_main(self):
        return self.main_choice == 'main'

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = (u'Отзывы')
        verbose_name_plural = (u'Отзыв')
# Create your models here.
