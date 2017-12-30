from django.conf.urls import url
from rest_framework import routers
from phone import views
from phone.views import mobileinfosViewSet
#from phone.views import Phone_infoViewSet, Phone_typeViewSet

router = routers.DefaultRouter()

router.register(r'mobileinfos', mobileinfosViewSet)

urlpatterns = router.urls
