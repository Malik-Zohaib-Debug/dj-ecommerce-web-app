import email
from enum import auto
from django.db import models

# Create your models here.
class RegisteredUser(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=15)
    password = models.CharField(max_length=12, default="")
    email_address = models.EmailField(max_length=30)
    user_address = models.CharField(max_length=150)
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    phone_number = models.BigIntegerField()
    user_zip = models.IntegerField()

    def __str__(self):
        return str(self.userID) + " " + self.firstname + " " + self.lastname + " " + self.email_address 
    