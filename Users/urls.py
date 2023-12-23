# urls.py (inside your 'Users' app)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolesViewSet, UserViewSet

router = DefaultRouter()
router.register(r'roles', RolesViewSet, basename='roles')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
