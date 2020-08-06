from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from string import Template
import json
from users import email
from users.email import Email
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import time
class regester():
       @csrf_exempt 
       def index(request):
              print("***")
              if request.method == 'POST':
                     body_unicode = request.body.decode('utf-8')
                     body_data = json.loads(body_unicode)
                     message = Email.makeTextEmail(body_data)
                     Email.sendEmail(body_data,message)
                     return HttpResponseRedirect('confirm')
              else :
                     return render(request, 'registration/regester.html')

       def confirm(request):
              if request.method == 'POST':
                     print("****")
                     body_unicode = request.body.decode('utf-8')
                     body_data = json.loads(body_unicode)
                     return HttpResponse("ok")
              else :
                     start_time = time.time()
                     print(start_time)
                     print(start_time -start_time)
                     while request.body.decode('utf-8')== null :
                            print("***")

                     ###duration = time.time() - start_time
                     return HttpResponse("ok")
                    

