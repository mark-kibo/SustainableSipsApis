from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Product
from .serializers import ProductSerializer
import uuid
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class ProductViewSet(ViewSet):

    queryset=Product.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def list_products(self, request):
        """
        get all products
        
        """

        # serializer
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


    def create_product(self, request):
        """
        create an instance of a product

        """
        # get request data
        data= request.data
        print(request)
        serializer=ProductSerializer(data=data)

      
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"errors": serializer.errors})
        
    
class ProductMutationViewSet(ViewSet):

    queryset=Product.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]

    def list_product(self, request, **kwargs):
        """get an instance of a product"""

        product_id= kwargs.get("id")

        product=Product.objects.get(id=uuid.UUID(product_id))

        serializer=ProductSerializer(product)

        if product:
            return Response(serializer.data)
        return Response({
            "error":"not found"
        })

    def update_product(self,request, **kwargs):
        """update product instance"""
        product_id = kwargs.get("id")
        try:

            if not product_id:
                return Response(
                    {"error":"Missing product Id"}
                )
            
            product = get_object_or_404(self.queryset, id=uuid.UUID(product_id))
            data = request.data
        

            if product:
                serializer=ProductSerializer(instance=product,
                                            data=data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response({
                        "error":serializer.errors
                        })

            return Response(
                {"error":"product does not exist"}
            )
        except:
            return Response(
                {"error":"transaction failed"}
            )

    

    def destroy_product(self, request, **kwargs):
        """ delete an instance of a product"""

        product_id= kwargs.get("id")

        if not product_id:
            return Response({
                "error":"Missing id"
            })
        

        product = Product.objects.get(id=uuid.UUID(product_id))
        print(product)

        if product:
            product.delete()
            return Response({
                "message":"deleted product successfully"
            })
        else:
            return Response({
                "error":"Product does not exist"
            })


