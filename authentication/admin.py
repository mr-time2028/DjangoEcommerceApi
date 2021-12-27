from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 
        'email', 
        'is_active', 
        'is_staff',  
        'is_superuser'
    )
    list_filter = (
        'username', 
        'is_superuser',
        'is_staff',
        'is_active'
    )

    fieldsets = (
        (
            'Personal Info', 
            {'fields': ('username', 'email', 'password')}
        ),
        (
            'Groups', 
            {'fields': ('groups',)}
        ),
        (
            'Permissions', 
            {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}
        ),
        (
            'Important dates', 
            {'fields': ('date_joined', 'last_login')}
        )
    )
    add_fieldsets = (
        (
            'Personal Info', 
            {'fields': ('username', 'email', 'password1', 'password2')}
        ),
        (
            'Permissions', 
            {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}
        ),
        (
            'Groups', 
            {'fields': ('groups',)}
        )
    )

    search_fields = (
        'username',
        'email'
    )