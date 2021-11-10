from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProductModelViewSet(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def get_object(self, queyset=None, **kwargs):
      item = self.kwargs.get('pk')
      return get_object_or_404(Product,pk=item)