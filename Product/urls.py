from django.urls import path
from .views import ProductViewSet, ProductMutationViewSet



urlpatterns=[
    path("list/", ProductViewSet.as_view({"get": "list_products", "post":"create_product"})),
    path("<str:id>/", ProductMutationViewSet.as_view({"patch": "update_product", "delete":"destroy_product", "get":"list_product"})),
    
]