# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import *
from review.models import *
from portfolio.models import *

admin.site.register(Review)
admin.site.register(Post)
admin.site.register(Portfolio)

