# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import *
from review.models import *
from portfolio.models import *
from grammars.models import *

class ImageInline(admin.TabularInline):
    model = ImageFolio

class FolioAdmin(admin.ModelAdmin):
    # fields = ['name','company','image','text']
    inlines = [ImageInline]


admin.site.register(Review)
admin.site.register(Post)

admin.site.register(Portfolio, FolioAdmin)

admin.site.register(Gram)

