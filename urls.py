from django.contrib import admin
from django.urls import path
from django.urls import path,include
from fee_api.views import StudentViewSet
from rest_framework import routers
from .import views


router= routers.DefaultRouter()
router.register(r'students', StudentViewSet )

urlpatterns = [
   
    path('',include(router.urls))
   
]