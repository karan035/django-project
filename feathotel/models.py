from django.db import models
from django.contrib.auth.models import User



class Enquery(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    contactNum=models.IntegerField()
    query=models.CharField(max_length=100)
    query_date = models.DateTimeField(auto_now_add=True)

