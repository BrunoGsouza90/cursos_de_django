from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from .models import CustomUser

# Registrar o modelo de usuário personalizado no admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# Registrar o modelo de usuário personalizado
admin.site.register(CustomUser, CustomUserAdmin)