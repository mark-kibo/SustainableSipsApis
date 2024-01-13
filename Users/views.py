from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Roles, OasisUser
from .serializers import RolesSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .TokenGeneration import get_tokens_for_user
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

# # JWT class to handle JWT token creating and refreshing
# class MyTokenObtainPairView(TokenObtainPairView):
#     permission_classes = (permissions.IsAuthenticated,)

# class MyTokenRefreshView(TokenRefreshView):
#     permission_classes = (permissions.IsAuthenticated,)
