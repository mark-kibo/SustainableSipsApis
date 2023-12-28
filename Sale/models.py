from django.db import models 
from Product.models import Product
import uuid

# Create your models here.

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, 
         editable = False)
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, related_name="sales", on_delete=models.SET_NULL,blank=False, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)