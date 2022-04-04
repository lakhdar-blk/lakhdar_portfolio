from distutils.command.upload import upload
from os import link
from turtle import title
from xml.parsers.expat import model
from django.db import models

# Create your models here.

class ContactMessage(models.Model):

    email       = models.EmailField(max_length=254)
    full_name   = models.CharField(max_length=50)
    reason      = models.CharField(max_length=50) 
    message     = models.TextField(max_length=1000)

    def __str__(self):
        return self.email
    

class Publication(models.Model):

    title       = models.CharField(max_length=500)
    journal     = models.CharField(max_length=200)
    doi         = models.CharField(max_length=200)
    year        = models.CharField(max_length=10)
    authors     = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title

class Degree(models.Model):

    title       = models.CharField(max_length=100)
    date        = models.CharField(max_length=10)
    univ        = models.CharField(max_length=255)
    years       = models.CharField(max_length=10)
    city        = models.CharField(max_length=100)
    country     = models.CharField(max_length=100)
    univ_image  = models.ImageField(upload_to ='static/images/')

    def __str__(self):
        return self.title

class Exper(models.Model):

    years   = models.CharField(max_length=10)
    company = models.CharField(max_length=100)
    post    = models.CharField(max_length=100)

    def __str__(self):
        return self.company   