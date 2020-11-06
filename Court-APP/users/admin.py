from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser, CustomAccountManager

admin.site.register(NewUser, CustomAccountManager)
