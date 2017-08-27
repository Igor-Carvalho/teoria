"""Modelos da aplicação artigos."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django import dispatch
from django.conf import settings
from django.contrib.sites.models import Site
from django.core import urlresolvers
from django.db import models
from django.db.models import signals
from inscritos.models import Inscrito
from model_utils.models import TimeStampedModel
from post_office import mail


class Etiqueta(TimeStampedModel):
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


class Categoria(TimeStampedModel):
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


class Artigo(TimeStampedModel):
    """Um artigo do blog."""

    class Meta:
        """Meta opções do modelo."""

        ordering = ['-id']

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='artigos')
    título = models.CharField('Título do artigo', max_length=100)
    slug = models.SlugField('Slug', max_length=100)
    conteúdo = models.TextField('Conteúdo do artigo')
    categorias = models.ManyToManyField(Categoria, related_name='artigos')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='artigos')

    histórico = AuditlogHistoryField()

    def get_absolute_url(self):
        """Obtém a url de detalhe para o artigo."""
        return urlresolvers.reverse('artigos:detalhe', args=[self.pk, self.slug])

    def enviar_notificação_de_email(self):
        """Notifica inscritos no boletim de notícias a respeito da criação de um novo artigo."""
        def construir_email(email, artigo):
            """Controe um email para ser enviado por mail.send_many."""
            return {
                'recipients': [email],
                'template': 'artigo_criado',
                'context': {'artigo': self, 'site': Site.objects.get_current()}
            }

        emails = map(lambda inscrito: inscrito.email, Inscrito.objects.filter(ativo=True))
        emails = map(lambda email: construir_email(email, self), emails)
        mail.send_many(emails)

    def __str__(self):
        """Representação textual do objeto."""
        return '{} por {}'.format(self.título, self.autor.get_full_name() or self.autor.username)


auditlog.register(Artigo)


def obter_caminho_da_imagem(imagem_artigo, nome_do_arquivo):
    """Obtém o caminho da imagem utilizando dados do artigo que ele referencia."""
    return 'artigos/imagens/{}/{}'.format(imagem_artigo.artigo.id, nome_do_arquivo)


class ImagemArtigo(TimeStampedModel):
    """Uma ou mais imagens pertencentes ao um artigo."""

    class Meta:
        """Meta opções do modelo."""

        verbose_name = 'Imagem de artigo'
        verbose_name_plural = 'Imagens de artigo'

    nome = models.CharField('Nome', max_length=100)
    caminho = models.ImageField('Caminho', upload_to=obter_caminho_da_imagem)
    artigo = models.ForeignKey(Artigo, related_name='imagens')

    histórico = AuditlogHistoryField()

    def __str__(self):
        """Representação textual do objeto."""
        return 'Imagem {} do artigo {}'.format(self.nome, self.artigo.título)


# Sinais
# ===========================================================================================================#

@dispatch.receiver(signals.post_save, sender=Artigo)
def enviar_notificação_de_email(sender, instance, created, **kwargs):
    """Notifica inscritos no boletim de notícias a respeito da criação de um novo artigo."""
    if created:
        instance.enviar_notificação_de_email()
