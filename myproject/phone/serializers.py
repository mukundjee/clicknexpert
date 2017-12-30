from rest_framework import serializers
#from models import Phone_info, Phone_type
from models import mobileinfos

class mobileinfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobileinfos
        #fields = ('name', 'manufacturer', 'screen_size', 'camera', 'cpu', 'os_version', 'phone_detail', 'launch_date', 'type')
        fields = ('mobile_name','phone_os', 'touchscreen', 'processor',\
        'sensors','screen_size', 'screen_resolution', 'display_features', \
        'fingerprint_sensor', 'gpu', 'ram', 'internal_memory', 'battery_capacity', \
        'weight', 'thickness', 'camera', 'camera_auto_focus', 'camera_flash', 'hd_video_recording', \
        'other_camera_features', 'secondary_camera', 'secondary_camera_features', 'bluetooth','usb', \
        'feature_4g', 'volte', 'feature_3g', 'feature_2g', 'wifi', 'compass', 'gps', 'dual_sim', 'nfc', 'dlna', 'more', 'price', \
        'app_store', 'launch', 'expandable_memory_slot', 'mobile_url')
