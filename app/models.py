from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    img = models.FileField(null=True,blank=True)

class Product(models.Model):
    img = models.FileField(null=True,blank=True)
    type = models.CharField(max_length=255,null=True,blank=True)
    dicount = models.CharField(max_length=255,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)