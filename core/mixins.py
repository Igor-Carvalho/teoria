"""Mixins da aplicação core."""

from django.contrib.auth import get_user_model


class AdminNoContextoMixin:
    """Obtém o admin do blog e o coloca no contexto da página."""

    def get_context_data(self, **kwargs):
        """Obtém o contexto da página."""
        contexto = super().get_context_data(**kwargs)
        contexto['usuário'] = get_user_model().objects.get(username='admin')
        return contexto
