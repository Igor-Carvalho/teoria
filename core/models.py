"""Modelos da aplicação core."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel


class Usuário(TimeStampedModel, AbstractUser):
    """Usuário base do projeto."""

    class Meta:
        """Model meta."""

        ordering = ['-id']

    histórico = AuditlogHistoryField()


auditlog.register(Usuário)
