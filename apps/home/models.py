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