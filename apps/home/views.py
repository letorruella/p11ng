# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.db.models import fields
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from .models import  Car, Accident, Maintenance
from django.core import serializers
from django.shortcuts import redirect


@login_required(login_url="/login/")
def index(request):
    events = [] # Maintenance.objects.all() + Accident.objects.all()
    for accident in Accident.objects.all():
        events.append(accident)
    for maintenace in Maintenance.objects.all():
        events.append(maintenace)
    context = {'segment': 'index', 'events':events}
    # print(cars)
    # content = {cars:cars}
    
    
    if request.user.is_superuser:
       return redirect('/admin')

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context,request))

def api_car(request):
    print('test')
    return JsonResponse({'hello':'hello'})


'''
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
'''