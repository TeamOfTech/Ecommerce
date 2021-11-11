from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TextField, URLField
from  django.core.validators import MinValueValidator
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.
class Category(models.Model):
  title = CharField(max_length=200)
  
  # Figure out out to organize subcategories

  # subcategory = ForeignKey('Category',on_delete=CASCADE)
  
  def __str__(self) -> str:
      return self.title

class Product(models.Model):
  name = CharField(max_length=250)
  image = URLField(null=True,blank=True)
  quantity = IntegerField(validators=[MinValueValidator(0)],default=0)
  category = ManyToManyField(Category, verbose_name='categories')
  description = TextField(blank=True,default='')
  price = IntegerField(validators=[MinValueValidator(0)],default=0)
  
  class Meta: # noqa
    verbose_name = 'Products'
    
  def __str__(self) -> str:
      return f'{self.name} ${self.price}'