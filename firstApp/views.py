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
import random
MY_ADDRESS = 'zkeshtkarz@gmail.com'
PASSWORD = input("please enter your password")
@csrf_exempt 
def index(request):
   if request.method == 'POST':
       body_unicode = request.body.decode('utf-8')
       body_data = json.loads(body_unicode)
       message = makeTextEmail(body_data)
       sendEmail(body_data,message)
       return HttpResponse("OK")
def makeTextEmail(body_data) :
       userName = body_data.get('userName')
       message = MIMEMultipart("alternative")
       message["Subject"] = "Confirm your account"
       html = """<html><body><p>Hello dear """+userName +"""<br>How are you? Tnx alot for regester .Your code is <br>"""+"""<font color="blue">"""+generateRandomCode()+"""</font>"""
       part2 = MIMEText(html, "html")
       message.attach(part2)
       return message 
def sendEmail(body_data,message):
       port = 465  # For SSL
       smtp_server = "smtp.gmail.com"
       context = ssl.create_default_context()
       with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(MY_ADDRESS, PASSWORD)
            receiver_email =body_data.get('email')
            server.sendmail(MY_ADDRESS,receiver_email, message.as_string())
def generateRandomCode():
    return str(random.randint(100_000,999_999))
