# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class Portfolio(models.Model):
    name = models.CharField(verbose_name=(u'Название сайта'), max_length=255)
    company = models.CharField(verbose_name=(u'Название компании') ,max_length=255)
    date = models.DateTimeField(verbose_name=(u'Дата'), auto_now_add=True)
    image = models.ImageField(verbose_name=(u'Скриншот сайта'), upload_to='portfolio', null=False)
    text = RichTextField()
    link = models.CharField(verbose_name=(u'ссылка'), max_length=155)

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

    class Meta:
        verbose_name = (u'Портфолио')
        verbose_name_plural = (u'Портфолио')