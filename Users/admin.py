from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import OasisUser, Roles
# Register your models here.


admin.site.register(OasisUser)
admin.site.register(Roles)
