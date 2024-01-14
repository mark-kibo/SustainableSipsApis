from django.db import models
import uuid
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, 
         editable = False)
    image = CloudinaryField('image', null=True)  # Store image files
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255, default="Alcohol")
    quantity = models.IntegerField(default=0)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Optional description


# class Category(models.model):
#     id = models.UUIDField(primary_key=True, default = uuid.uuid4,editable = False)
#     name = models.CharField(max_length=255, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

