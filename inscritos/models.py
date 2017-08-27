"""Modelos da aplicação inscritos."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.contrib.sites import shortcuts
from django.db import models
from django.utils import crypto
from model_utils.models import TimeStampedModel
from post_office import mail


def criar_chave():
    """Cria uma chave aleatória."""
    return crypto.get_random_string(64)


class Inscrito(TimeStampedModel):
    """Um leitor inscrito no blog, identificado pelo seu email."""

    class Meta:
        """Meta opções do modelo."""

        ordering = ['id']

    ativo = models.BooleanField(default=False)
    email = models.EmailField()
    chave = models.CharField(max_length=64, unique=True, null=True, default=criar_chave)

    histórico = AuditlogHistoryField()

    def enviar_email_de_confirmação(self, request):
        """Envia um email de confirmação para que o usuário possa ativar sua conta."""
        if not self.ativo:
            mail.send(
                recipients=[self.email],
                template='ativação_de_inscrito',
                context={'inscrito': self, 'site': shortcuts.get_current_site(request)},
                priority='now',
            )

    def ativar(self):
        """Ativa um inscrito para que o mesmo possa receber notificações."""
        self.ativo = True
        self.chave = None
        self.save()

    def __str__(self):
        """Representação textual do objeto."""
        return 'Inscrito nº {}: {}'.format(self.id, self.email)


auditlog.register(Inscrito)
