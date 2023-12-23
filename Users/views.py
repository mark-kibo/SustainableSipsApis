from django.shortcuts import render
from rest_framework import viewsets
from .models import Roles, User
from .serializers import RolesSerializer, UserSerializer

# Create your views here.
class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
