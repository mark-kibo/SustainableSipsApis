from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductViewSet(ViewSet):

    def get_products(self, request):
        queryset=Product.objects.all()

        # serializer
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)