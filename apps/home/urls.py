# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db.models import fields
from django.urls import path, re_path, include
from apps.home import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import Revenue

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class RevenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Revenue
        fields = ['revenue','date']

# ViewSets define the view behavior.
class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'revenue', RevenueViewSet)

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # path('api/', views.api_car),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
