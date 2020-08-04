
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import smtplib, ssl
import json
import random
class Email():
       def makeTextEmail(body_data) :
                     userName = body_data.get('userName')
                     message = MIMEMultipart("alternative")
                     message["Subject"] = "Confirm your account"
                     html = """<html><body><p>Hello dear """+userName +"""<br>How are you? Tnx alot for regester .Your code is <br>"""+"""<font color="blue">"""+Email.generateRandomCode()+"""</font>"""
                     part2 = MIMEText(html, "html")
                     message.attach(part2)
                     return message 
       def sendEmail(body_data,message):
                     MY_ADDRESS = 'zkeshtkarz@gmail.com'
                     PASSWORD = input("please enter your password")
                     port = 465
                     smtp_server = "smtp.gmail.com"
                     context = ssl.create_default_context()
                     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                            server.login(MY_ADDRESS, PASSWORD)
                            receiver_email =body_data.get('email')
                            server.sendmail(MY_ADDRESS,receiver_email, message.as_string())
       def generateRandomCode():
                     return str(random.randint(100_000,999_999))