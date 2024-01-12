from os import truncate
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Product.models import Product
from Sale.models import Sale
from django.db.models import Count
from .serializers import CategoryProductCountSerializer, CategoryResultSerializer, LowQuantityProductSerializer, LowQuantityResultSerializer, TotalProductsSerializer

from django.db.models import Sum, Count, F
from django.db.models.functions import TruncDate
from datetime import datetime, timedelta
from django.db.models import Count, Sum, Case, When, Value
from django.db.models.functions import TruncDate
from django.utils import timezone
from datetime import timedelta
# Create your views here.


class SummaryViewSet(ViewSet):

    permission_classes=[IsAuthenticatedOrReadOnly]


    def summary_details(self,request):
        """
        Get summary details for the landing page
        
        """

        # Categories with total number of products
        category_result = Product.objects.values('category').annotate(product_count=Count('id'))
        category_serializer = CategoryProductCountSerializer(category_result, many=True)

        # Products with quantity less than 10
        low_quantity_result = Product.objects.filter(quantity__lt=10)
        low_quantity_serializer = LowQuantityProductSerializer(low_quantity_result, many=True)


        # Calculate the start and end of the current week (Monday to Sunday)
        today = timezone.now()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        # Generate a list of all days in the current week
        all_days_in_week = [start_of_week + timedelta(days=i) for i in range(7)]

        # Query to get sales data for each day of the week, including days with no sales
        sales_by_day = Sale.objects.filter(
            created_at__gte=start_of_week,
            created_at__lte=end_of_week
        ).annotate(
            truncated_date=TruncDate('created_at')
        ).values('truncated_date').annotate(
            total_sales=Count('id'),
            total_amount=Sum('sale_amount')
        )

        # Create a dictionary to store sales data for each day
        sales_data_by_day = {entry['truncated_date']: entry for entry in sales_by_day}

        # # Create a list to store results for all days in the week
        result = []

        print(type(sales_by_day))

        for day in all_days_in_week:
            # Format the date
            formatted_date = timezone.localtime(day).strftime('%Y-%m-%d')
            
            # Get sales data for the current day or default to zero
            sales_data = sales_data_by_day.get(day.date(), {'total_sales': 0, 'total_amount': 0})
            print(sales_data_by_day)
            result.append({
                'date': formatted_date,
                'total_sales': sales_data['total_sales'],
                'total_amount': sales_data['total_amount']
            })

        print(result)
        #Print or return the result as needed
        #print(sales_data_by_day)    
        #print(result)

        response_data = {
            'category_product_count': category_serializer.data,
            'low_quantity_products': low_quantity_serializer.data,
            'weekly_sales': result
        }
        
        return Response(response_data)

    def summary(self,request):
        """
        Get summary details 
        
        """
        category_result = Product.objects.values('category').distinct().count()
        category_serializer = CategoryResultSerializer({'category_count': category_result})
        
        total_products = Product.objects.count()
        products_serializer = TotalProductsSerializer({'total_products': total_products})

        low_quantity_result = Product.objects.filter(quantity__lt=10)
        low_quantity_count = low_quantity_result.count()
        low_quatity_serializer = LowQuantityResultSerializer({'low_quantity_count': low_quantity_count})

        response_data = {
            'categories': category_serializer.data,
            'products': products_serializer.data,
            'low_stock': low_quatity_serializer.data,
        }

        return Response(response_data)


