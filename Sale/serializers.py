from rest_framework.serializers import ModelSerializer, SerializerMethodField
from datetime import datetime
from .models import Sale



class SalesSerializer(ModelSerializer):
    date_created = SerializerMethodField(read_only=True)
    date_updated = SerializerMethodField(read_only=True)
    product_name=SerializerMethodField(read_only=True)
  

    class Meta:
        model = Sale
        fields = ("id", "sale_amount", "date_created", "date_updated", "product_name", "product") 

    def get_date_created(self, instance):
        formatted_date = datetime.strftime(instance.created_at, "%Y-%m-%d %H:%M:%S")
        return formatted_date
    
    def get_date_updated(self, instance):
        formatted_date = datetime.strftime(instance.updated_at, "%Y-%m-%d %H:%M:%S")
        return formatted_date
    
    def get_product_name(self, instance):
        return instance.product.name if instance.product else None
        

        
