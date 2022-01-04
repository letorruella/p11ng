from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from apps.home.models import Car
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def api_car(request):
    car = serializers.serialize('json', Car.objects.all()) 
    print("hi")
    return JsonResponse(car, safe=False)