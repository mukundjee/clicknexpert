# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
#from .models import Phone_info, Phone_type
#from .serializers import Phone_infoSerializer, Phone_typeSerializer
from .models import Phone_info, Phone_type, Phone_camera, Screen_size, Phone_cpu, Manufacturer, Version_os
from .serializers import Phone_infoSerializer, Phone_typeSerializer, Phone_cameraSerializer, Screen_sizeSerializer, Phone_cpuSerializer, ManufacturerSerializer, Version_osSerializer
# Create your views here.

class Phone_infoViewSet(viewsets.ModelViewSet):

     queryset = Phone_info.objects.all()
     serializer_class = Phone_infoSerializer
     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
     filter_fields =('id',)
     ordering =('price',)

# class Phone_infoViewSet(viewsets.ModelViewSet):
#
#     queryset = Phone_info.objects.all()
#     serializer_class = Phone_infoSerializer
#     filter_fields =('name',)
    #test for details
    #@detail_route()
    #def phone_list(self, request, pk=None):
#         name = self.get_object() # retrieve an object by pk provided
#         schedule = Version_os.objects.filter(show_phone=phone).distinct()
#         schedule_json = Version_osSerializer(schedule, many=True)
#         return Response(schedule_json.data)

class Phone_typeViewSet(viewsets.ModelViewSet):
    queryset = Phone_type.objects.all()
    serializer_class = Phone_typeSerializer

class Phone_cameraViewSet(viewsets.ModelViewSet):
    queryset = Phone_camera.objects.all()
    serializer_class = Phone_cameraSerializer

class Screen_sizeViewSet(viewsets.ModelViewSet):
    queryset = Screen_size.objects.all()
    serializer_class = Screen_sizeSerializer

class Phone_cpuViewSet(viewsets.ModelViewSet):
    queryset = Phone_cpu.objects.all()
    serializer_class = Phone_cpuSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class Version_osViewSet(viewsets.ModelViewSet):
    queryset = Version_os.objects.all()
    serializer_class = Version_osSerializer

#class UserListView(generics.ListAPIView):
#    queryset = Phone_info.objects.all()
#    serializer_class = Phone_infoSerializer
#    filter_backends = (filters.SearchFilter,)

#    search_fields = ('name', 'os_version')

#test through filter
#class PhoneFilter(django_filters.FilterSet):
#    phone = django_filters.CharFilter(name="name")

#    class Meta:
#        model = Phone_info
#        fields = ['price', 'os_version', 'manufacturer']

#class PhoneListView(generics.ListAPIView):
#    queryset = Phone_info.objects.all()
#    serializer_class = Phone_infoSerializer
#    filter_backends = (DjangoFilterBackend,)
#    filter_fields = ('name', 'os_version')
    #filter_backends = (filters.SearchFilter,)
    #filter_class = PhoneFilter
    #return queryset
    #search_fields = ('name', 'os_version')
#test query
#class PhoneListView(generics.ListAPIView):
#    serializer_class = Phone_infoSerializer

#    def get_queryset(self):
#        """
#        Optionally restricts the returned purchases to a given user,
#        by filtering against a `username` query parameter in the URL.
#        """
#        queryset = Phone_info.objects.all()
#        name = self.request.QUERY_PARAMS.get('name', None)
#        if name is not None:
#            queryset = queryset.filter(name=name)
#        return queryset
#class Phone_listViewSet(viewsets.ModelViewSet):
#       queryset = Phone_info.objects.all()
#       serializer_class = Phone_infoSerializer

#test for details
#@detail_route()
#def phone_list(self, request, pk=None):
#        name = self.get_object() # retrieve an object by pk provided
#        schedule = Version_os.objects.filter(show__phone=phone).distinct()
#        schedule_json = Version_osSerializer(schedule, many=True)
#        return Response(schedule_json.data)

#class Phone_listViewSet(generics.ListAPIView):
#     serializer_class = Phone_infoSerializer

#     def get_queryset(self):

#         name = Phone_info.objects.get(id=self.kwargs['name'])

#         return Version_os.objects.filter(name=name).distinct()
