from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request
from datetime import *
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)
    accno = models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=1000)
    telephone = models.IntegerField(null=True,blank=True)
    dob=models.DateField(default=date.today)
    profile_created_by=models.CharField(max_length=250,default="staff")
    profile_created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
# class User(models.Model):
#     def get_absolute_url(self):
#         return reverse('user-detail', kwargs={"pk": self.pk})
# class cuser(models.Model):
#     # objects = None
#     username=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="tag")
#     accno = models.IntegerField()
    # email_confirmed = models.BooleanField(default=False)
#     accno=models.IntegerField(null=True,blank=True)
#
#     address=models.CharField(max_length=1000)
#     Telephone = models.IntegerField()
#     dob=models.DateField
#     isaccountactive = models.BooleanField(default=False)
#     profile_created_by=models.CharField(max_length=250)
#     profile_created_date=models.DateTimeField(auto_now_add=True)



    # def __str__(self):
    #     return self.username
# class curru(models.Model):
#     # objects = None
#     username=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="tag")
#     email_confirmed = models.BooleanField(default=False)
#     def __str__(self):
#         return self.username
#
# @receiver(post_save, sender=User)
# def update_user_curru(sender, instance, created, **kwargs):
#     if created:
#         curru.objects.create(username=instance)
#     instance.curru.save()
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication,related_name="tag1")

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


