from django.urls import path, include
from rest_framework import routers
from .views import UserAPIView

app_name = 'user'

router = routers.DefaultRouter()
router.register('users', UserAPIView)