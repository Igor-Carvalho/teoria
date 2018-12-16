"""Configurações de teste."""

from .development import * # noqa F403

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
AUTH_PASSWORD_VALIDATORS = []

MIDDLEWARE = MIDDLEWARE.copy() # noqa F405
MIDDLEWARE.remove('core.middleware.HttpsOnlyMiddleware')
