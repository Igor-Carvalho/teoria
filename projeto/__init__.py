"""Carrega módulos automaticamente durante inicialização da aplicação."""

from .celery import app as celery_app

__all__ = ('celery_app',)
