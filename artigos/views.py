"""Visões da aplicação artigos."""

from core import mixins
from django.views import generic

from . import models


class ArtigosLista(mixins.AdminNoContextoMixin, generic.ListView):
    """Carrega artigos na página inicial."""

    model = models.Artigo
    queryset = models.Artigo.objects.all()
    context_object_name = 'artigos'
    template_name = 'artigos/artigos.html'


artigos_lista = ArtigosLista.as_view()


class ArtigosDetalhe(mixins.AdminNoContextoMixin, generic.DetailView):
    """Visão para um determinado artigo."""

    model = models.Artigo
    context_object_name = 'artigo'
    template_name = 'artigos/artigo.html'


artigos_detalhe = ArtigosDetalhe.as_view()
