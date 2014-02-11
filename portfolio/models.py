# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Portfolio(models.Model):
    name = models.CharField(verbose_name=(u'Название сайта'), max_length=255)
    company = models.CharField(verbose_name=(u'Название компании') ,max_length=255)
    date = models.DateTimeField(verbose_name=(u'Дата'), auto_now_add=False)
    image = models.ImageField(verbose_name=(u'Скриншот сайта'), upload_to='portfolio', null=False)
    text = RichTextField()
    # link = models.CharField(verbose_name=(u'ссылка'), max_length=155)
    slug = AutoSlugField(editable=True, default='default', verbose_name=(u'ссылка'))

    main_choice = models.CharField(
        max_length=7,
        verbose_name=(u'На главную'),
        choices=(
            ('notmain', 'нет'),
            ('main', 'да'),
        ),
        default='notmain'
    )

    def portfolio_in_main(self):
        return self.main_choice == 'main'

    def __unicode__(self):
        return self.name

    def get_pictures(self):
        return self.pictures.all()

    def get_absolute_url(self):
        return 'portfolio/%s' % self.slug

    class Meta:
        verbose_name = (u'Портфолио')
        verbose_name_plural = (u'Портфолио')


class ImageFolio(models.Model):
    title = models.CharField(u'Название фотографии', max_length=100)
    album = models.ForeignKey(Portfolio, related_name='pictures', verbose_name=u'Альбом работы')
    img = models.ImageField(u'Фото', upload_to='portfolio')
    class Meta:
        ordering = ['title']
        verbose_name = u'Фото'
        verbose_name_plural = u'Фотографии'
    def __unicode__(self):
        return self.title

