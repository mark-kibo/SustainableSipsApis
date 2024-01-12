# serializers.py
from rest_framework import serializers
from Product.models import Product

class CategoryProductCountSerializer(serializers.Serializer):
    category = serializers.CharField()
    product_count = serializers.IntegerField()

class LowQuantityProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity']

class SalesByDaySerializer(serializers.Serializer):
    date = serializers.DateField()
    total_sales = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

class CategoryResultSerializer(serializers.Serializer):
    category_count = serializers.IntegerField()

class TotalProductsSerializer(serializers.Serializer):
    total_products = serializers.IntegerField()

class LowQuantityResultSerializer(serializers.Serializer):
    low_quantity_count = serializers.IntegerField()