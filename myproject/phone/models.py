# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from .views import MultipleModelAPIView
from django.db import models
#from decimal import Decimal

# Create your models here.

class mobileinfos(models.Model):
    mobile_name = models.CharField(max_length=80)
    phone_os = models.CharField(max_length=60)
    touchscreen = models.CharField(max_length=50)
    processor = models.CharField(max_length=60)
    sensors = models.CharField(max_length=200)
    screen_size = models.CharField(max_length=50)
    screen_resolution = models.CharField(max_length=60)
    display_features = models.CharField(max_length=200)
    fingerprint_sensor = models.CharField(max_length=60)
    gpu = models.CharField(max_length=60)
    ram = models.CharField(max_length=60)
    internal_memory = models.CharField(max_length=60)
    battery_capacity = models.CharField(max_length=60)
    weight = models.CharField(max_length=60)
    thickness = models.CharField(max_length=60)
    camera = models.CharField(max_length=60)
    camera_auto_focus = models.CharField(max_length=50)
    camera_flash = models.CharField(max_length=50)
    hd_video_recording = models.CharField(max_length=50)
    other_camera_features = models.CharField(max_length=200)
    secondary_camera = models.CharField(max_length=60)
    secondary_camera_features = models.CharField(max_length=200)
    bluetooth = models.CharField(max_length=50)
    usb = models.CharField(max_length=50)
    feature_4g = models.CharField(max_length=50)
    volte = models.CharField(max_length=50)
    feature_3g = models.CharField(max_length=50)
    feature_2g = models.CharField(max_length=50)
    wifi = models.CharField(max_length=50)
    compass = models.CharField(max_length=50)
    gps = models.CharField(max_length=50)
    dual_sim = models.CharField(max_length=50)
    nfc = models.CharField(max_length=50)
    dlna = models.CharField(max_length=50)
    more = models.CharField(max_length=200)
    price = models.CharField(max_length=60)
    app_store = models.CharField(max_length=60)
    launch = models.CharField(max_length=60)
    expandable_memory_slot = models.CharField(max_length=60)
    mobile_url = models.CharField(max_length=200)
    class Meta:
        verbose_name = "mobileinfo"
        verbose_name_plural = "mobileinfos"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %s %s \
                %s %s %s %s %s %s %s %s %s %s \
                %s %s %s %s %s %s %s %s %s %s \
                %s %s %s %s %s %s %s %s %s %s' \
                % (self.mobile_name, self.phone_os, self.touchscreen, self.processor, self.sensors, self.Screen_size,\
                 self.screen_resolution, self.display_features, self.fingerprint_sensor, self.gpu, self.ram, self.internal_memory,\
                 self.battery_capacity, self.weight, self.thickness, self.camera, self.camera_auto_focus, self.camera_flash,\
                 self.hd_video_recording, self.other_camera_features, self.secondary_camera, self.secondary_camera_features,\
                 self.bluetooth, self.usb, self.feature_4g, self.volte, self.feature_3g, self.feature_2g, self.wifi, self.compass, self.gps,\
                 self.dual_sim, self.nfc, self.dlna, self.more, self.price, self.app_store, self.launch, self.expandable_memory_slot,\
                 self.mobile_url)
