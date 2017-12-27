# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from .views import MultipleModelAPIView
from django.db import models
#from decimal import Decimal

# Create your models here.

class Version_os(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Version's"

    def __unicode__(self):
        #return '%s %s' % (self.name, self.size)
        return '%s' % (self.version)

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturer's"

    def __unicode__(self):
        #return '%s %s' % (self.name, self.size)
        return '%s' % (self.manufacturer)

class Screen_size(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Screen_size"
        verbose_name_plural = "'Screen_size's"

    def __unicode__(self):
        #return '%s %s' % (self.name, self.size)
        return '%s' % (self.size)

class Phone_camera(models.Model):
    name = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Phone_camera"
        verbose_name_plural = "Phone_camera's"

    def __unicode__(self):
        return '%s' % (self.camera)

class Phone_cpu(models.Model):
    name = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Phone_cpu"
        verbose_name_plural = "Phone_cpu's"

    def __unicode__(self):
        #return '%s %s' % (self.name, self.cpu)
        return '%s' % (self.cpu)

class Phone_type(models.Model):
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Phone_type"
        verbose_name_plural = "Phone_type's"
    def __unicode__(self):
        return '%s' % (self.type)

class Phone_info(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    screen_size = models.ForeignKey(Screen_size)
    camera = models.ForeignKey(Phone_camera)
    cpu = models.CharField(max_length=50)
    os_version = models.ForeignKey(Version_os)
    phone_detail = models.CharField(max_length=200)
    launch_date = models.DateField(max_length=20)
    type = models.ForeignKey(Phone_type)
    class Meta:
        verbose_name = "Phone_info"
        verbose_name_plural = "Phone_info's"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %s %s' % (self.name, self.manufacturer, self.price, self.screen_size, self.camera, self.cpu, self.os_version, self.phone_detail, self.launch_date, self.type)
        #return '%s %s %s %s %s %s %s %s %s' % (self.name, self.manufacturer, self.screen_size, self.camera, self.cpu, self.os_version, self.phone_detail, self.launch_date, self.type)
