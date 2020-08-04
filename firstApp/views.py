from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.views.decorators.csrf import csrf_exempt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.views.generic import TemplateView
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import json

MY_ADDRESS = 'zkeshtkarz@gmail.com'
PASSWORD = '97243057zK'
@csrf_exempt 
def index(request):
   if request.method == 'POST':
       port = 465  # For SSL
       smtp_server = "smtp.gmail.com"
       context = ssl.create_default_context()
       with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(MY_ADDRESS, PASSWORD)
            user = json.loads(request.body)
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            receiver_email =body_data.get('email')
            server.sendmail(MY_ADDRESS,receiver_email, 'HELLO')
       return HttpResponse("OK")

    
# Create your views here.
