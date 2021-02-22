# from importlib._common import _
from urllib import request

from django.http import *
from django.db import models
from django.urls import reverse
# from pyparsing import unicode
from datetime import *
# Create your models here.
class Trans_type(models.Model):
    Trans_symbol = models.CharField(max_length=250)
    Type= models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Type
    class Meta:
        unique_together = ("Trans_symbol", "Type")
class Account(models.Model):
    Name=models.CharField(max_length=200)
    Accno=models.IntegerField()
    Dfield = models.DateField(default=date.today)
    Amount=models.IntegerField()
    # Amt_d=models.IntegerField()
    # Amt_c=models.IntegerField()
    Type=models.ForeignKey(Trans_type, on_delete=models.CASCADE)