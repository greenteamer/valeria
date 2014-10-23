# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Review(models.Model):
    name = models.CharField(verbose_name=(u'Имя'), max_length=155)
    company = models.CharField(verbose_name=(u'Компания'), max_length=155, null=True)
    date = models.DateTimeField(verbose_name=(u'Дата'), auto_now_add=True)
    text = RichTextField()
    image = models.ImageField(verbose_name=(u'Фото'), upload_to='reviews', null=True)
    slug = AutoSlugField(editable=True, default="default")

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

    def get_absolute_url(self):
        return '/review/%s/' % self.slug

    class Meta:
        verbose_name = (u'Отзывы')
        verbose_name_plural = (u'Отзыв')
# Create your models here.

class ReviewGallery(models.Model):
    image = models.ImageField(upload_to='reviews/reviews_gallery', verbose_name='Галерея отзыва')
    review = models.ForeignKey(Review, verbose_name='для какого отзыва')

    def url_self(self):
        return 'media/%s' % self.image