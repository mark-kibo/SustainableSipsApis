from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, User



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

class Roles(models.Model):
    role_name = models.CharField(max_length=255)



class SustainableUser(AbstractBaseUser):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    phone_number = models.CharField(max_length=20,unique=True)
    role = models.ForeignKey('Roles', on_delete=models.SET_NULL, null=True, blank=True)
    
    USERNAME_FIELD = 'phone_number'
   
    



    def set_password_hash(self, plain_password):
        self.password = make_password(plain_password)
        return self.password

    def check_password_hash_match(self, plain_password):
        return check_password(plain_password, self.password)

