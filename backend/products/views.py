from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProductModelViewSet(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  # def create(self, request, *args, **kwargs):
  #     print(request.data)
  #     categories = request.data['categories'].split(',')
  #     request['category'] = []
  #     for cat in categories:
  #       _,category = Category.objects.get_or_create(name=cat)
  #       request['category'].append(category)
        
  #     del request.data['categories']
  #     return super().create(request, *args, **kwargs)
  
  def get_object(self, queyset=None, **kwargs):
      item = self.kwargs.get('pk')
      return get_object_or_404(Product,pk=item)
    
class CategoryModelViewSet(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
  def get_object(self, queyset=None, **kwargs):
      category_name = self.kwargs.get('name')
      return get_object_or_404(Category,name=category_name)