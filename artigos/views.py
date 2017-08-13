"""Visões da aplicação artigos."""

import logging

from rest_framework import generics, viewsets

from . import models, serializers

logger = logging.getLogger(__name__)


class ArtigoVisões(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    """Visão para obtenção de artigos."""

    queryset = models.Artigo.objects.all()

    def get_serializer_class(self):
        """Obtém o serializador de acordo com a solicitação."""
        if self.action == 'list':
            logger.debug('"Obtendo lista de artigos, retornando serializador para conteúdo reduzido"')
            return serializers.ArtigoSerializadorConteúdoReduzido

        logger.debug('"Obtendo artigo, retornando serializador padrão"')
        return serializers.ArtigoSerializador
