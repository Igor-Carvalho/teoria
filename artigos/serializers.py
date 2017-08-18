"""Serializadores da aplicação artigos."""

from django import template
from django.utils import text
from rest_framework import serializers

from . import models


class EtiquetaSerializador(serializers.ModelSerializer):
    """Serializador de etiquetas."""

    class Meta:
        """Meta opções do modelo."""

        model = models.Etiqueta
        fields = '__all__'


class CategoriaSerializador(serializers.ModelSerializer):
    """Serializador de categorias."""

    class Meta:
        """Meta opções do modelo."""

        model = models.Etiqueta
        fields = '__all__'


class ArtigoSerializador(serializers.ModelSerializer):
    """Serializador de artigos."""

    class Meta:
        """Meta opções do modelo."""

        model = models.Artigo
        fields = '__all__'

    etiquetas = EtiquetaSerializador(many=True, read_only=True)
    categorias = CategoriaSerializador(many=True, read_only=True)
    autor = serializers.StringRelatedField(source='autor.get_full_name')

    def _obter_conteúdo_renderizado(self, artigo):
        """Obtém o conteúdo do artigo renderizado corretamente."""
        conteúdo_renderizado = template.Template(artigo.conteúdo).render(template.Context({'artigo': artigo}))
        return conteúdo_renderizado

    def to_representation(self, artigo):
        """Retorna o conteúdo rst já renderizado."""
        dicionário = super(ArtigoSerializador, self).to_representation(artigo)
        dicionário['conteúdo'] = self._obter_conteúdo_renderizado(artigo)
        return dicionário


class ArtigoSerializadorConteúdoReduzido(ArtigoSerializador):
    """Serializador de artigos com o conteúdo reduzido para exibição em listas."""

    def to_representation(self, artigo):
        """Reduz o conteúdo do artigo para exibição."""
        dicionário = super(serializers.ModelSerializer, self).to_representation(artigo)

        total_de_palavras = self.context['request'].query_params.get('total_de_palavras', '15')
        conteúdo_renderizado = self._obter_conteúdo_renderizado(artigo)
        conteúdo_renderizado_truncado = text.Truncator(conteúdo_renderizado).words(
            int(total_de_palavras),
            html=True,
            truncate=' ...'
        )
        dicionário['conteúdo'] = conteúdo_renderizado_truncado
        return dicionário
