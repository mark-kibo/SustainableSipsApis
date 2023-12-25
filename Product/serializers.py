from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product
from datetime import datetime
from Sale.serializers import SalesSerializer




class ProductSerializer(ModelSerializer):
    sales= SalesSerializer(many=True, read_only=True)


    class Meta:
        model=Product
        fields=(
                "id",
                "image",
                "name", 
                "quantity", 
                "buying_price", 
                "selling_price", 
                "description" ,
                "sales"
            )




   


