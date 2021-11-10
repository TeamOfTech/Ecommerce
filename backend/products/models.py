from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from  django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
  name = CharField(max_length=250)
  description = TextField(blank=True,default='')
  price = IntegerField(validators=[MinValueValidator(0)],default=0)
  
  class Meta: # noqa
    verbose_name = 'Products'
    
  def __str__(self) -> str:
      return f'{self.name} ${self.price}'