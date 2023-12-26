from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product
from datetime import datetime
from Sale.serializers import SalesSerializer




class ProductSerializer(ModelSerializer):
    sales= SalesSerializer(many=True, read_only=True)
    image_url=SerializerMethodField(read_only=True)


    class Meta:
        model=Product
        fields=(
                "id",
                "image_url",
                "name", 
                "quantity", 
                "buying_price", 
                "selling_price", 
                "description" ,
                "sales"
            )

    def get_image_url(self, instance):
        return instance.image.url


   


