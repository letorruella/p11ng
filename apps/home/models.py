# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=150, help_text='Car Brand')
    car_model = models.CharField(max_length=150, help_text='Car Model')
    investor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_brand} - {self.car_model} {self.investor.username}'



class Revenue(models.Model):
    revenue = models.IntegerField(blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField()
    event_type = models.CharField( default='revenue' ,max_length=150 ,blank=True, null=True)

    

class Accident(models.Model):
    FAULT=[
        ('me',"me"),
        ("thirdparty", "thirdparty")
    ]
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    accident = models.CharField(help_text="Where accident occur?",max_length=150 ,blank=True, null=True)
    fault = models.CharField(help_text="Who's at fault?", max_length=150, choices=FAULT, blank=True, null=True)
    totaled = models.CharField(help_text="Was car totaled?", max_length=150,blank=True, null=True)
    photo = models.ImageField(upload_to='cars', help_text='Upload all images and documents related to accident',blank=True, null=True)
    date = models.DateField()
    event_type = models.CharField( default='accident' ,max_length=150 ,blank=True, null=True)
    
    

class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    type = models.CharField(help_text="what type of maintance?", max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to='cars', help_text='Upload all images and documents related to accident',blank=True, null=True)
    value = models.IntegerField(help_text="How much?",blank=True, null=True)
    cost = models.IntegerField(help_text="Cost?",blank=True, null=True)
    approve = models.BooleanField(help_text="Approved?", blank=True, null=True )
    event_type = models.CharField( default='maintenance' ,max_length=150 ,blank=True, null=True)

    