# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from blog.models import Post
from review.models import *
from portfolio.models import *

class FolioView(TemplateView):
    template_name = 'folio.html'

    def get_context_data(self, **kwargs):
        context = super(FolioView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        context['portfolios'] = Portfolio.objects.filter(main_choice='main')
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context

class FolioDetail(DetailView):
    template_name = 'folio_detail.html'
    model = Portfolio
