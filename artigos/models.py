"""Modelos da aplicação artigos."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel


class Etiqueta(TimeStampedModel, models.Model):
    """Uma ou mais etiquetas (tags) que um artigo pode ter."""

    class Meta:
        """Meta opções do modelo."""

        ordering = ['-id']

    nome = models.CharField('Nome', max_length=100)

    histórico = AuditlogHistoryField()

    def __str__(self):
        """Representação textual do objeto."""
        return self.nome


auditlog.register(Etiqueta)


class Categoria(TimeStampedModel, models.Model):
    """Uma ou mais categorias que um artigo pode pertencer."""

    class Meta:
        """Meta opções do modelo."""

        ordering = ['-id']

    nome = models.CharField('Nome', max_length=100)

    histórico = AuditlogHistoryField()

    def __str__(self):
        """Representação textual do objeto."""
        return self.nome


auditlog.register(Categoria)


class Artigo(TimeStampedModel, models.Model):
    """Um artigo do blog."""

    class Meta:
        """Meta opções do modelo."""

        ordering = ['-id']

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='artigos')
    título = models.CharField('Título do artigo', max_length=100)
    conteúdo = models.TextField('Conteúdo do artigo')
    categorias = models.ManyToManyField(Categoria, related_name='artigos')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='artigos')

    histórico = AuditlogHistoryField()

    def __str__(self):
        """Representação textual do objeto."""
        return '{} por {}'.format(self.título, self.autor.get_full_name())


auditlog.register(Artigo)
