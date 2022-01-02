# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Car, Revenue, Accident
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model')

class EventAdmin(admin.ModelAdmin):
    pass

class AccidentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)
admin.site.register(Revenue, EventAdmin)
admin.site.register(Accident, AccidentAdmin)