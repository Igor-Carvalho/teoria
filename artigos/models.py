"""Modelos da aplicação artigos."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django import dispatch, urls
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import signals
from model_utils.models import TimeStampedModel
from post_office import mail

from inscritos.models import Inscrito


class Etiqueta(TimeStampedModel):
    """Uma ou mais etiquetas (tags) que um artigo pode ter."""

    nome = models.CharField('Nome', max_length=100)

    histórico = AuditlogHistoryField()

    class Meta:
        """Meta opções do modelo."""

        ordering = ['-id']

    def __str__(self):
        """Representação textual do objeto."""
        return self.nome


auditlog.register(Etiqueta)


class Categoria(TimeStampedModel):
    """Uma ou mais categorias que um artigo pode pertencer."""

    nome = models.CharField('Nome', max_length=100)

    histórico = AuditlogHistoryField()

    class Meta:
        """Meta opções do modelo."""

        ordering = ['-id']

    def __str__(self):
        """Representação textual do objeto."""
        return self.nome


auditlog.register(Categoria)


class Artigo(TimeStampedModel):
    """Um artigo do blog."""

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='artigos', on_delete=models.CASCADE)
    título = models.CharField('Título do artigo', max_length=100)
    slug = models.SlugField('Slug', max_length=100)
    conteúdo = models.TextField('Conteúdo do artigo')
    categorias = models.ManyToManyField(Categoria, related_name='artigos')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='artigos')

    histórico = AuditlogHistoryField()

    class Meta:
        """Meta opções do modelo."""

        ordering = ['-id']

    def get_absolute_url(self):
        """Obtém a url de detalhe para o artigo."""
        return urls.reverse('artigos:detalhe', args=[self.pk, self.slug])

    def enviar_notificação_de_email(self):
        """Notifica inscritos no boletim de notícias a respeito da criação de um novo artigo."""
        def construir_email(email):
            """Controe um email para ser enviado por mail.send_many."""
            return {
                'recipients': [email],
                'template': 'artigo_criado',
                'context': {'artigo': self, 'site': Site.objects.get_current()}
            }

        emails = map(lambda inscrito: construir_email(inscrito.email), Inscrito.objects.filter(ativo=True))
        mail.send_many(emails)
        mail.send_queued()

    def __str__(self):
        """Representação textual do objeto."""
        nome_autor = self.autor.get_full_name() or self.autor.username
        return f'{self.título} por {nome_autor}'


auditlog.register(Artigo)


def obter_caminho_da_imagem(imagem_artigo, nome_do_arquivo):
    """Obtém o caminho da imagem utilizando dados do artigo referenciado."""
    return f'artigos/imagens/{imagem_artigo.artigo.id}/{nome_do_arquivo}'


class ImagemArtigo(TimeStampedModel):
    """Uma ou mais imagens pertencentes ao um artigo."""

    nome = models.CharField('Nome', max_length=100)
    caminho = models.ImageField('Caminho', upload_to=obter_caminho_da_imagem)
    artigo = models.ForeignKey(Artigo, related_name='imagens', on_delete=models.CASCADE)

    histórico = AuditlogHistoryField()

    class Meta:
        """Meta opções do modelo."""

        verbose_name = 'Imagem de artigo'
        verbose_name_plural = 'Imagens de artigo'

    def __str__(self):
        """Representação textual do objeto."""
        return f'Imagem {self.nome} do artigo {self.artigo.título}'


auditlog.register(ImagemArtigo)


# Sinais
# ===========================================================================================================#

@dispatch.receiver(signals.post_save, sender=Artigo)
def enviar_notificação_de_email(sender, instance, created, **kwargs):
    """Notifica inscritos no boletim de notícias a respeito da criação de um novo artigo."""
    if created:
        instance.enviar_notificação_de_email()
