# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from blog.models import Post
from review.models import *
from portfolio.models import *
from grammars.models import *

from feedback.forms import ContactForm, MiniForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.conf import settings

from dajaxice.core import dajaxice_functions
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

# from slider.models import Slider
# from game.models import Game
# from user_profile.models import Supernumerary


# class MainView(TemplateView): #старая вьюха главной страницы
#     template_name = 'base.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MainView, self).get_context_data()
#         context['posts'] = Post.objects.all()
#         context['reviews'] = Review.objects.all()
#         context['portfolios'] = Portfolio.objects.filter(main_choice='main')
#         context['grams'] = Gram.objects.all()
#         # context['slides'] = Slider.objects.all()
#         # context['games'] = Game.objects.all()
#         # context['supernumeraries'] = Supernumerary.objects.all()
#         return context

# class SaitView(TemplateView):
#     template_name = 'sait.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(SaitView, self).get_context_data()
#         context['grams'] = Gram.objects.all()
#         # context['slides'] = Slider.objects.all()
#         # context['games'] = Game.objects.all()
#         # context['supernumeraries'] = Supernumerary.objects.all()
#         return context

def mainpage(request):
    if request.method == 'POST':
        form = MiniForm(request.POST)
        subject = u'Valeria заявка от %s' % request.POST['sender']
        message = u'Телефон: %s \n Имя: %s' % (request.POST['phone'], request.POST['sender'])
        if form.is_valid():
            send_mail(subject, message, 'teamer777@gmail.com', ['forward.70@yandex.ru'], fail_silently=False)
            return HttpResponseRedirect('/')
        else:
            form = ContactForm({'phone': u'Введите свой телефон',})
            posts = Post.objects.all()
            grams = Gram.objects.all()
            reviews = Review.objects.all()
            portfolios = Portfolio.objects.filter(main_choice='main')
            return render(request, 'base.html', {
                'form': form,
                'posts' : posts,
                'grams': grams,
                'reviews' : reviews,
                'portfolios' : portfolios,
            })
    else:
        form = MiniForm()
        posts = Post.objects.all()
        grams = Gram.objects.all()
        reviews = Review.objects.all()
        portfolios = Portfolio.objects.filter(main_choice='main')
    return render(request, 'base.html', {
        'form': form,
        'posts' : posts,
        'grams': grams,
        'reviews' : reviews,
        'portfolios' : portfolios,
    })

def sozdanie(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = u'7works заявка от %s' % request.POST['subject']
        message = u'Сообщение: %s \n %s \n телефон: %s \n почта: %s' % (request.POST['message'], request.POST['subject'], request.POST['phone'], request.POST['sender'])
        if form.is_valid():
            send_mail(subject, message, 'teamer777@gmail.com', ['forward.70@yandex.ru'], fail_silently=False)
            return HttpResponseRedirect('/sozdanie-saitov/')
        else:
            form = ContactForm({'phone': u'Введите свой телефон',})
            grams = Gram.objects.all()
            return render(request, 'sait.html', {
                'form': form,
                'grams': grams,
            })
    else:
        form = ContactForm()
        grams = Gram.objects.all()
    return render(request, 'sait.html', {
        'form': form,
        'grams': grams,
    })

def prodvijenie(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = u'7works заявка от %s' % request.POST['subject']
        message = u'Сообщение: %s \n %s \n телефон: %s \n почта: %s' % (request.POST['message'], request.POST['subject'], request.POST['phone'], request.POST['sender'])
        if form.is_valid():
            send_mail(subject, message, 'teamer777@gmail.com', ['forward.70@yandex.ru'], fail_silently=False)
            return HttpResponseRedirect('/prodvijenie/')
        else:
            form = ContactForm({'phone': u'Введите свой телефон',})
            grams = Gram.objects.all()
            return render(request, 'prodvijenie.html', {
                'form': form,
                'grams': grams,
            })
    else:
        form = ContactForm()
        grams = Gram.objects.all()
    return render(request, 'prodvijenie.html', {
        'form': form,
        'grams': grams,
    })


class MobileView(TemplateView):
    template_name = 'mobile.html'

    def get_context_data(self, **kwargs):
        context = super(MobileView, self).get_context_data()
        context['grams'] = Gram.objects.all()
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context

# class ContactView(TemplateView):
#     template_name = 'contact.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ContactView, self).get_context_data()
#         context['grams'] = Gram.objects.all()
#         # context['slides'] = Slider.objects.all()
#         # context['games'] = Game.objects.all()
#         # context['supernumeraries'] = Supernumerary.objects.all()
#         return context