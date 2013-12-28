# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    subject = forms.CharField(label=u'Ваше имя', max_length=255, required=False)
    phone = forms.CharField(label=u'Ваш телефон', max_length=255)
    sender = forms.EmailField(label=u'Ваша почта', required=False)
    message = forms.CharField(label=u'Сообщение', required=False, max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':50}))
