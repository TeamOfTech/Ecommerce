from django.urls import path
from .views import ProductModelViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',ProductModelViewSet,basename='products')

urlpatterns = router.urls