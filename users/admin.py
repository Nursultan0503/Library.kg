from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'city', 'is_verified', 'is_active', 'date_joined')
    list_filter = ('is_verified', 'is_active', 'gender')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    exclude = ('password', 'verification_code', 'user_permissions', 'groups')
