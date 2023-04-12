from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class Team(models.Model):
    regnumber = models.IntegerField(null=True)
    enrollment1 = models.CharField(max_length=30)
    admission1 = models.CharField(max_length=30)
    name1 = models.CharField(max_length=30)
    email1 = models.EmailField()
    phone1= models.CharField(max_length=30)
    enrollment2 = models.CharField(max_length=30)
    admission2= models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    email2 = models.EmailField()
    phone2= models.CharField(max_length=30) 
    enrollment3 = models.CharField(max_length=30)
    admission3 = models.CharField(max_length=30)
    name3 = models.CharField(max_length=30)
    email3 = models.EmailField()
    phone3= models.CharField(max_length=30)
    def __str__(self):
        return self.name1

# Create your models here.



