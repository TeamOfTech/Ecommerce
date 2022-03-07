from django.urls import path
from .views import CategoryModelViewSet, ProductModelViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", ProductModelViewSet, basename="products")
router.register("category", CategoryModelViewSet, basename="category")

urlpatterns = router.urls
