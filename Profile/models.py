from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from Userdetail.models import User
from django.http import request


from django.dispatch import receiver

# Create your models here.

#
# class profile(models.Model):
#
#     username=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="tag")
#     accno=models.IntegerField()
#
#     address=models.CharField(max_length=1000)
#     Telephone = models.IntegerField()
#     dob=models.DateField
#     profile_created_by=models.CharField(max_length=250)
#     profile_created_date=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.username
