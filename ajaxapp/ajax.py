#-*-coding:utf-8-*-
from django.utils import simplejson
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from feedback.forms import ContactForm
from django.core.mail import send_mail

@dajaxice_register
# def sayhello(request):
#     return simplejson.dumps({'message':'Hello World'})

def send_form(request, form):
    dajax = Dajax()
    form = ContactForm(deserialize_form(form))
    dajax.remove_css_class('#my_form .loading', 'hidden')
    if form.is_valid():
        dajax.remove_css_class('#my_form input', 'error')
        dajax.remove_css_class('#status', 'hidden')

        result = u'Отправляем сообщение'
        dajax.assign('#status', 'value', result)
        subject = u'7works заявка от %s' % form.cleaned_data.get('subject')
        message = u'Сообщение: %s \n %s \n телефон: %s \n почта: %s' % (form.cleaned_data.get('message'), form.cleaned_data.get('subject'), form.cleaned_data.get('phone'), form.cleaned_data.get('sender'))
        send_mail(subject, message, 'teamer777@gmail.com', ['forward.70@yandex.ru'], fail_silently=False)

        dajax.remove_css_class('#status', 'hidden')
        # result = u'Сообщение отправлено'
        # dajax.assign('#status', 'value', result)
        dajax.remove_css_class('#message_show', 'hidden')
        dajax.script('closemodal()')



        # dajax.redirect('/', delay=2000)
        # dajax.code('$(".close").click()')

    else:
        dajax.remove_css_class('#my_form input', 'error')
        dajax.remove_css_class('#status', 'hidden')
        result = u'Введите данные'
        dajax.assign('#status', 'value', result)
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error, 'error')



    dajax.add_css_class('div .loading', 'hidden')
    return dajax.json()

# def load_form(request, form):
#     dajax = Dajax()
#     dajax.alert("Form is_valid(), your phone is: %s" % form.cleaned_data.get('phone'))
#
#     return dajax.json()