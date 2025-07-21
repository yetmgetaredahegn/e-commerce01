from django.shortcuts import render
from django.core.mail import send_mail, mail_admins,BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage

def say_hello(request):
    try: 
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name':'Yetm'}
        )
        message.send(['but@yetm.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
