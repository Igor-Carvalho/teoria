"""Módulo contém views genéricas ou globais ao projeto."""

from django.contrib.auth import get_user_model
from django.views import generic


class IndexView(generic.TemplateView):
    """
    Página base da aplicação.

    Esta página contém a infraestrutura SPA (Single Page Application): scripts, estilos, etc.
    """

    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        """Obtém o contexto da página."""
        contexto = super().get_context_data(**kwargs)
        contexto['usuário'] = get_user_model().objects.get(username='admin')
        return contexto
