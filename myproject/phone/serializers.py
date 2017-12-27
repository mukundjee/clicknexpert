from rest_framework import serializers
#from models import Phone_info, Phone_type
from models import Phone_info, Phone_type, Phone_camera, Screen_size, Phone_cpu, Manufacturer, Version_os

class Phone_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone_info
        #fields = ('name', 'manufacturer', 'screen_size', 'camera', 'cpu', 'os_version', 'phone_detail', 'launch_date', 'type')
        fields = ('name', 'manufacturer', 'price', 'screen_size', 'camera', 'cpu', 'os_version', 'phone_detail', 'launch_date', 'type')

class Phone_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone_type
        fields = ('type', )

class Phone_cameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone_camera
        fields = ('name', 'camera')
        #fields = ('camera', )
class Screen_sizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen_size
        fields = ('name', 'size')

class Phone_cpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone_cpu
        fields = ('name', 'cpu')

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'manufacturer')

class Version_osSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version_os
        fields = ('name', 'version')
