# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from blog.models import Post
from review.models import *
from portfolio.models import *
# from slider.models import Slider
# from game.models import Game
# from user_profile.models import Supernumerary


class MainView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        context['portfolios'] = Portfolio.objects.filter(main_choice='main')
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context

class SaitView(TemplateView):
    template_name = 'sait.html'

    def get_context_data(self, **kwargs):
        context = super(SaitView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context

class ProdvijenieView(TemplateView):
    template_name = 'prodvijenie.html'

    def get_context_data(self, **kwargs):
        context = super(ProdvijenieView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context



class MobileView(TemplateView):
    template_name = 'mobile.html'

    def get_context_data(self, **kwargs):
        context = super(MobileView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context