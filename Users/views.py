from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Roles, OasisUser
from .serializers import RolesSerializer, UserSerializer, CreateUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .TokenGeneration import get_tokens_for_user
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
# Create your views here.
class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    
    serializer_class = RolesSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = OasisUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
class newUserViewSet(viewsets.ViewSet):
    queryset = OasisUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


    def post_user(self, request, **kwargs):
        data= request.data

        user=get_object_or_404(OasisUser, username=data.get("username"))

        if user:
            if user.check_password_hash_match(data.get("password")):
                tokens=get_tokens_for_user(user)
                print(tokens)
                
                return Response({
                    "token": tokens,
                    "user_role": user.role.role_name
                })
            return Response({
                "error": "Invalid password"
            })
        return Response({
                "error": "Invalid credentials"
            })


class CreateUserViewSet(viewsets.ViewSet):

    queryset = OasisUser.objects.all()
    serializer_class = CreateUserSerializer


    def create_user(self, request, **kwargs):

        data= request.data
        data=data.get("user")

        role= get_object_or_404(Roles, role_name=data.get("role"))
        print(role)
        if role:
            data["role"] = role.id
            serializer = self.serializer_class(data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.validated_data["password"] = make_password(serializer.validated_data["password"])
                serializer.save()
                return Response(
                    serializer.data
                )
        return Response({
            "error":"No such role exists"
        })

# # JWT class to handle JWT token creating and refreshing
# class MyTokenObtainPairView(TokenObtainPairView):
#     permission_classes = (permissions.IsAuthenticated,)

# class MyTokenRefreshView(TokenRefreshView):
#     permission_classes = (permissions.IsAuthenticated,)
