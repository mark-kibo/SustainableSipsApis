from django.db import models
# from django.contrib.auth.models import BaseUserManager
import uuid
# from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)


class CustomUserManager(UserManager):
    # def _create_user(self, email, password, **extra_fields):
    #     if not email:
    #         raise ValueError("You have not provided a valid e-mail address")
        
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)

    #     return user
    
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("You have not provided your username")
        user=self.model(username=username,  **extra_fields)
        user.set_password(password)
        user.save()
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, password, **extra_fields)

class Roles(models.Model):
    role_name = models.CharField(max_length=255)





# class SustainableUser(models.Model):
#     user_id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False
#     )
#     username= models.CharField(max_length=255, unique=True, null=True, blank=True, default='')
#     email= models.EmailField(max_length=255, unique=True, blank=False)
#     password= models.CharField(max_length=255, unique=True)
#     phone_number = models.CharField(max_length=20)
#     role = models.ForeignKey('Roles', on_delete=models.SET_NULL, null=True, blank=True)

#     date_joined=models.DateTimeField(default=timezone.now)
#     date_joined=models.DateTimeField(blank=True, null=True)

#     is_staff=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)
#     is_anonymous=models.BooleanField(default=False)
#     is_authenticated=models.BooleanField(default=True)
    
    



  

#     def set_password_hash(self, plain_password):
#         self.password = make_password(plain_password)
#         return self.password

#     def check_password_hash_match(self, plain_password):
#         return check_password(plain_password, self.password)



class OasisUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    phone_number = models.CharField(max_length=20)
    role = models.ForeignKey('Roles', on_delete=models.SET_NULL, null=True, blank=True)

    date_joined=models.DateTimeField(default=timezone.now)
    date_joined=models.DateTimeField(blank=True, null=True)


    USERNAME_FIELD="username"
    REQUIRED_FIELDS=[]


    objects=CustomUserManager()



    def set_password_hash(self, plain_password):
        self.password = make_password(plain_password)
        return self.password

    def check_password_hash_match(self, plain_password):
        return check_password(plain_password, self.password)


    def __str__(self):
        return self.username




