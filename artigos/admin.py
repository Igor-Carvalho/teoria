"""Administração da aplicação artigos."""

from django.contrib import admin

from . import models


@admin.register(models.Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    """Configuração do modelo Etiqueta na interface admin."""


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Configuração do modelo Categoria na interface admin."""


@admin.register(models.Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    """Configuração do modelo Artigo na interface admin."""
