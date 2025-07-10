from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'phone', 'is_verified', 'is_staff', 'is_active')
    list_filter = ('is_verified', 'is_staff', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': (
                'phone',
                'profile_image',
                'address',
                'is_verified',
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': (
                'email',
                'phone',
                'profile_image',
                'address',
                'is_verified',
            ),
        }),
    )

    search_fields = ('email', 'username', 'phone')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
