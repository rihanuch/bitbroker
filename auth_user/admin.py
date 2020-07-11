from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auth_user.models import User


class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email',)
    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'telegram_user',
                'password',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'telegram_user',
                'password',
            )
        }),
    )


admin.site.register(User, CustomUserAdmin)
