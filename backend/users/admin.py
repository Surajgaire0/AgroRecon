from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_from=CustomUserCreationForm
    form=CustomUserChangeForm
    models=CustomUser
    list_display=('username','first_name','last_name','email')

admin.site.register(CustomUser,CustomUserAdmin)