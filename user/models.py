from django.db import models
class User(models.Model):
     name=models.CharField(max_length=100)
     email = models.CharField(unique=True)
     phone = models.CharField(max_length=18 , unique=True)
     user_name = models.CharField(max_length=100 , unique=True)
     profile_image = models.CharField(max_length=100)
     date_joined = models.DateTimeField(auto_now_add=True ,null =True)
     date_updated = models.DateTimeField(auto_now=True ,null =True)