from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.utils.html import escape, mark_safe
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.dispatch import receiver
import re
from django.utils import timezone





class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name





class Universite(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Domaine(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name



class Student(models.Model):

    name = models.CharField(max_length=270,verbose_name= u"Last name  ")
    prenom = models.CharField(max_length=270,verbose_name= u"First name   ")
    adresse_email = models.EmailField(max_length=100,verbose_name=u"email ",)
    numero_telephone=models.IntegerField(verbose_name= u"Phone number  ",  null=True, blank=True)
    composante = models.CharField(max_length=100,verbose_name=u"University  ")
    domaine = models.CharField(max_length=100,verbose_name=u"Domaine  ")
    fonction = models.ManyToManyField(Subject, verbose_name= u"Function  ", related_name='interested_student')
    autre = models.CharField(max_length=270,verbose_name= u"If other ",  null=True, blank=True)
    choice_field = models.CharField(max_length=270,verbose_name= u" ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    name_adre = models.CharField(max_length=270,verbose_name= u"I want to work with (First and last Name) ", help_text=" PS: you can only choose one Person to work with",  null=True, blank=True)
    prenom_adre = models.CharField(max_length=270,verbose_name= u"First name   ", null=True, blank=True)
    adresse_email_adre = models.EmailField(max_length=100,verbose_name=u"Email address of the person you want to work with.",null=True, blank=True)
   
    def __str__(self):
        if self.name==None:
           return "ERROR-CUSTOMER NAME IS NULL"
        return self.name

