from django.db import models

class User(models.Model):
    
    userName = models.CharField(max_length=100)
    email =  models.EmailField(blank=True,primary_key = True)
    passWord =  models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20, unique=True)
# Create your models here.
