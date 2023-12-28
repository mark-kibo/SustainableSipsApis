from django.shortcuts import render
from rest_framework import viewsets
from .models import Roles, SustainableUser
from .serializers import RolesSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    
    serializer_class = RolesSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = SustainableUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# JWT class to handle JWT token creating and refreshing
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.IsAuthenticated,)

class MyTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.IsAuthenticated,)
