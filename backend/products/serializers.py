from django.db.models.fields import CharField
from rest_framework import fields, serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category

class ProductSerializer(serializers.ModelSerializer):
  
  categories = CategorySerializer(many=True,read_only=True)
  
  class Meta:
    fields = '__all__'
    model=Product