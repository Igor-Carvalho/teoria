"""Configuração de administração da aplicação core."""

from django.contrib.admin import register
from django.contrib.auth import admin, get_user_model


@register(get_user_model())
class UserModelAdmin(admin.UserAdmin):
    """User admin."""
