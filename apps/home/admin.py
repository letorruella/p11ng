# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Car, Event
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)
admin.site.register(Event, EventAdmin)