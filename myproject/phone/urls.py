from django.conf.urls import url
from rest_framework import routers
from phone import views
#from phone.views import Phone_infoViewSet, Phone_typeViewSet, Phone_cameraViewSet, Screen_sizeViewSet, Phone_cpuViewSet, ManufacturerViewSet, Version_osViewSet
from phone.views import  Phone_infoViewSet, Phone_typeViewSet, Phone_cameraViewSet, Screen_sizeViewSet, Phone_cpuViewSet, ManufacturerViewSet, Version_osViewSet
#, Phone_listViewSet
#from phone.views import Phone_infoViewSet, Phone_typeViewSet

router = routers.DefaultRouter()

router.register(r'Phone_info', Phone_infoViewSet)
router.register(r'Phone_type', Phone_typeViewSet)
router.register(r'Phone_camera', Phone_cameraViewSet)
router.register(r'Screen_size', Screen_sizeViewSet)
router.register(r'Phone_cpu', Phone_cpuViewSet)
router.register(r'Manufacturer', ManufacturerViewSet)
router.register(r'Version_os', Version_osViewSet)
#router.register(r'Phonelist', Phone_listViewSet)
#router.register(r'date-list', views.Phone_listViewSet)

urlpatterns = router.urls
