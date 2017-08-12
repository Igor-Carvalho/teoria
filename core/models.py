"""Modelos da aplicação core."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.contrib.auth import models


class User(models.AbstractUser):
    """Usuário base do projeto."""

    history = AuditlogHistoryField()

    class Meta:
        """Model meta."""

        verbose_name = 'Usuário'


auditlog.register(User)
