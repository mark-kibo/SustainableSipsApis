from django.shortcuts import render, get_object_or_404
from .models import Sale
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from Product.models import Product
from Product.serializers import ProductSerializer
from .serializers import SalesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import uuid
# Create your views here.


class ListAllSalesViewSet(ViewSet):
    queryset = Sale.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    

    def list_sales(self, request):

        """get all sales availble"""
        serializer=SalesSerializer(self.queryset, many=True)


        return Response(serializer.data)





class SaleViewSet(ViewSet):

    queryset=Sale.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]

    def create_sale(self, request, **kwargs):
        """create a sale instance - should reduce a product quantity"""

        data= request.data
        
        # print(data)
        product_id=kwargs.get("id")


        product=get_object_or_404(Product, id=uuid.UUID(product_id))
        print(product)

        if product:
            if product.quantity >= int(data.get("quantity")) and product.quantity > 0:
                # Create a sale instance
                sale_data = {
                    "sale_amount": data.get("sale_amount"),
                    "product": product.id
                 
                }
                print(sale_data)

                sale_serializer = SalesSerializer(data=sale_data)

                if sale_serializer.is_valid(raise_exception=True):
                    sale_serializer.save()

                    product.quantity = product.quantity - int(data.get("quantity"))

                    product.save()

                    # Serialize and return the updated product
                    product_serializer = ProductSerializer(product)
                    return Response(product_serializer.data)
                return Response({"error":sale_serializer.errors})
            return Response({
                "error": "Insufficient product quantity"
            })
                    
        else:
            return Response({
                "error":"product does not exist"
            })




    def update_sale(self, request, **kwargs):

        """update an instance of a sale"""
        data= request.data
   

        sale_id= kwargs.get("id")

        sale=Sale.objects.get(id=uuid.UUID(sale_id))

        if not sale:
            return Response({"error": "sale does not exist"})

        sale_serializer=SalesSerializer(data=data, instance=sale, partial=True)

        if sale_serializer.is_valid(raise_exception=True):
            sale_serializer.save()
            return Response(sale_serializer.data)
        else:
            return Response({
                "error":sale_serializer.errors
            })

    def get_sale(self, request, **kwargs):
        """get an instance of a sale"""

        sale_id= kwargs.get("id")

        sale=Sale.objects.get(id=uuid.UUID(sale_id))

        serializer=SalesSerializer(sale)

        if sale:
            return Response(serializer.data)
        return Response({
            "error":"not found"
        })



    


