# serializers.py
from rest_framework import serializers
from .models import Roles, SustainableUser

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SustainableUser
        fields = ['user_id','username',  'phone_number', 'role']
