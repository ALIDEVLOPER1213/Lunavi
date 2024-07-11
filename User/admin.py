from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserManager

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')

admin.site.register(User, CustomUserAdmin)
