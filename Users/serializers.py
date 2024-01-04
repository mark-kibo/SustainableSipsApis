# serializers.py
from rest_framework import serializers
from .models import Roles, OasisUser

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OasisUser
        fields = ['id', 'username',  'phone_number', 'role']
