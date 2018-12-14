"""Modelos da aplicação inscritos."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django import urls
from django.contrib.sites.models import Site
from django.db import models
from django.utils import crypto
from model_utils.models import TimeStampedModel
from post_office import mail


def criar_chave():
    """Cria uma chave aleatória."""
    return crypto.get_random_string(64)


class Inscrito(TimeStampedModel):
    """Um leitor inscrito no blog, identificado pelo seu email."""

    ativo = models.BooleanField(default=False)
    email = models.EmailField()
    chave = models.CharField(max_length=64, unique=True, null=True, default=criar_chave)

    histórico = AuditlogHistoryField()

    class Meta:
        """Meta opções do modelo."""

        ordering = ['id']

    def enviar_email_de_confirmação(self):
        """Envia um email de confirmação para que o usuário possa ativar sua conta."""
        context = {'inscrito': self, 'site': Site.objects.get_current(), 'link': self.obter_link_ativação()}
        mail.send(recipients=[self.email], template='ativação_de_inscrito', context=context, priority='now')

    def obter_link_ativação(self):
        """Obtém o link para ativação de contas."""
        return f'{urls.reverse("v1:inscrito-list")}ativar/?chave={self.chave}'

    def ativar(self):
        """Ativa um inscrito para que o mesmo possa receber notificações."""
        self.ativo = True
        self.chave = None
        self.save()

    def __str__(self):
        """Representação textual do objeto."""
        return 'Inscrito nº {}: {}'.format(self.id, self.email)


auditlog.register(Inscrito)
