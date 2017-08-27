"""Visões da aplicação inscritos."""

from django import http, shortcuts
from rest_framework import decorators, mixins, response, viewsets

from . import models, serializers


class InscritoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Conjunto de visões para um inscrito."""

    serializer_class = serializers.InscritoSerializer
    queryset = models.Inscrito.objects.all()

    @decorators.list_route(methods=['GET'])
    def ativar(self, request, pk=None):
        """Ativa um usuário."""
        chave = request.query_params.get('chave', None)
        if not chave:
            raise http.Http404()

        inscrito = shortcuts.get_object_or_404(models.Inscrito, chave=chave)
        inscrito.ativar()
        return response.Response({'mensagem': 'Inscrito ativado com sucesso.'})
