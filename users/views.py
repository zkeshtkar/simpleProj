from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.views.decorators.csrf import csrf_exempt


from django.views.generic import TemplateView
from string import Template

import json
from users import email
from users.email import Email

class regester():
       @csrf_exempt 
       def index(request):
              if request.method == 'POST':
                     body_unicode = request.body.decode('utf-8')
                     body_data = json.loads(body_unicode)
                     message = Email.makeTextEmail(body_data)
                     Email.sendEmail(body_data,message)
                     return HttpResponse("OK")
       

