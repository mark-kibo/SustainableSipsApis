# urls.py (inside your 'Users' app)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolesViewSet, UserViewSet, MyTokenObtainPairView, MyTokenRefreshView

router = DefaultRouter()
router.register(r'roles', RolesViewSet, basename='roles')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
