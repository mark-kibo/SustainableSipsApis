from django.urls import path
from .views import  ListAllSalesViewSet, SaleViewSet



urlpatterns=[
   
    path("sale/<str:id>/", SaleViewSet.as_view({"post": "create_sale",  "patch":"update_sale"})),
    path("all/", ListAllSalesViewSet.as_view({"get": "list_sales"}))
]