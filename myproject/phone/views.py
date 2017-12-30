# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import django_filters.rest_framework
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
#from .models import Phone_info, Phone_type
#from .serializers import Phone_infoSerializer, Phone_typeSerializer
from .models import mobileinfos
from .serializers import mobileinfosSerializer

# Create your views here.

class mobileinfosViewSet(viewsets.ModelViewSet):

     queryset = mobileinfos.objects.all()
     serializer_class = mobileinfosSerializer
     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
     filter_fields =('mobile_name','phone_os')
