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


class Event(models.Model):
    EVENT_TYPE = [
    ('maintenance', 'Maintenance'),
    ('accident', 'Accident'),
    ('revenue', 'Revenue'),
    ]

    revenue = models.IntegerField(blank=True, null=True)
    event_type = models.CharField(max_length=150, choices=EVENT_TYPE, help_text='Event Type', null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField() 