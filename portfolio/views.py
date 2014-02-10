# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from blog.models import Post
from review.models import *
from portfolio.models import *
from grammars.models import *

class FolioView(TemplateView):
    template_name = 'folio.html'

    def get_context_data(self, **kwargs):
        context = super(FolioView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        context['portfolios'] = Portfolio.objects.filter(main_choice='main')
        return context

class FolioDetail(DetailView):
    template_name = 'folio_detail.html'
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(FolioDetail, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        context['portfolios'] = Portfolio.objects.all().order_by('date')
        context['grams'] = Gram.objects.all()
        return context