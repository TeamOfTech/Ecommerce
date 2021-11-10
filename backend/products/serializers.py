from rest_framework import fields, serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model=Product