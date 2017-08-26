"""Visões da aplicação artigos."""

from django.contrib.postgres.search import SearchVector
from django.views import generic

from . import models


class ArtigosLista(generic.ListView):
    """Carrega artigos na página inicial."""

    model = models.Artigo
    queryset = models.Artigo.objects.all()
    context_object_name = 'artigos'
    template_name = 'artigos/artigos.html'
    paginate_by = 3
    page_kwarg = 'página'

    def get_queryset(self):
        """Utiliza o parâmetro busca filtrar os registros."""
        queryset = super(ArtigosLista, self).get_queryset()
        busca = self.request.GET.get('busca', None)
        if busca:
            fields = 'conteúdo', 'título', 'categorias__nome', 'etiquetas__nome'
            queryset = queryset.annotate(search=SearchVector(*fields)).filter(search=busca).distinct('id')

        return queryset


artigos_lista = ArtigosLista.as_view()


class ArtigosDetalhe(generic.DetailView):
    """Visão para um determinado artigo."""

    model = models.Artigo
    context_object_name = 'artigo'
    template_name = 'artigos/artigo.html'


artigos_detalhe = ArtigosDetalhe.as_view()
