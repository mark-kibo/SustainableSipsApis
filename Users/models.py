from django.db import models
import uuid
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# from django.contrib.auth.models import BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         # your implementation

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)



# class SustainableSipsUser(AbstractBaseUser):
#     user_id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False
#     )
#     username= models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20)
#     role = models.ForeignKey('Roles', on_delete=models.SET_NULL, blank=True)


#     def set_password_hash(self, plain_password):
#         self.password = make_password(plain_password)
#         return self.password

#     def check_password_hash_match(self, plain_password):
#         return check_password(plain_password, self.password)


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class Roles(models.Model):
    role_name = models.CharField(max_length=255)





class SustainableSipsUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username= models.CharField(max_length=255, unique=True, null=True, blank=True, default='')
    email= models.EmailField(max_length=255, unique=True, blank=False)
    password= models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    role = models.ForeignKey('Roles', on_delete=models.SET_NULL, null=True, blank=True)

    date_joined=models.DateTimeField(default=timezone.now)
    date_joined=models.DateTimeField(blank=True, null=True)

    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_anonymous=models.BooleanField(default=False)
    is_authenticated=models.BooleanField(default=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    objects=UserManager()

    USERNAME_FIELD='username'
    EMAIL_FIELD='email'
    # PASSWORD_FIELD='password'
    REQUIRED_FIELDS=[]


  

    def set_password_hash(self, plain_password):
        self.password = make_password(plain_password)
        return self.password

    def check_password_hash_match(self, plain_password):
        return check_password(plain_password, self.password)

