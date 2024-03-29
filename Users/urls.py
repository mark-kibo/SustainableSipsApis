# urls.py (inside your 'Users' app)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolesViewSet, UserViewSet, newUserViewSet, CreateUserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'roles', RolesViewSet, basename='roles')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', newUserViewSet.as_view({"post":"post_user"}), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('new/user/', CreateUserViewSet.as_view({"post":"create_user"}), name='new_user'),
   
    
   
]


