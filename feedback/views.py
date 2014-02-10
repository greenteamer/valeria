# -*- coding: utf-8 -*-
from feedback.forms import ContactForm
from blog.models import *
from grammars.models import *
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = u'7works заявка от %s' % request.POST['subject']
        message = u'Сообщение: %s \n %s \n телефон: %s \n почта: %s' % (request.POST['message'], request.POST['subject'], request.POST['phone'], request.POST['sender'])
        if form.is_valid():
            send_mail(subject, message, 'teamer777@gmail.com', ['forward.70@yandex.ru'], fail_silently=False)
            return HttpResponseRedirect('/kontakty/')
        else:
            form = ContactForm({'phone': u'Введите свой телефон',})
            # return HttpResponseRedirect('/kontakty/', {'form':form.errors})
            # return form.errors
            return render(request, 'contact.html', {
                'form': form,
            })
    else:
        form = ContactForm()
        grams = Gram.objects.all()

    return render(request, 'contact.html', {
        'form': form,
        'grams': grams,
    })

