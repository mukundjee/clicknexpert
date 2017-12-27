# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Phone_info
from .models import Phone_type
from .models import Phone_camera
from .models import Screen_size
from .models import Phone_cpu
from .models import Manufacturer
from .models import Version_os

# Register your models here.

admin.site.register(Phone_info)
admin.site.register(Phone_type)
admin.site.register(Phone_camera)
admin.site.register(Screen_size)
admin.site.register(Phone_cpu)
admin.site.register(Manufacturer)
admin.site.register(Version_os)
