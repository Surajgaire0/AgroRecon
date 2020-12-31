from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('address', 'profile_picture')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
