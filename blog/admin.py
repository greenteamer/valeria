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

class ReviewGalleryAdmin(admin.StackedInline):
    model = ReviewGallery

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    inlines = [ReviewGalleryAdmin,]
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Review, ReviewAdmin)
admin.site.register(Post)

admin.site.register(Portfolio, FolioAdmin)

admin.site.register(Gram)

