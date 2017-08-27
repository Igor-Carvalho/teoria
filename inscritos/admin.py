"""Administração da aplicação inscritos."""

from django.contrib import admin

from . import models


@admin.register(models.Inscrito)
class InscritoAdmin(admin.ModelAdmin):
    """Configuração administrativa para inscritos."""
