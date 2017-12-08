"""Core middlewares."""

from django import http
from django.conf import settings


class HttpsOnlyMiddleware:
    """
    Bloqueia solicitações que não sejam https.

    Django permite redirecionar automaticamente solicitações http para https, mas este middleware é util
    contra scanners variados que inspecionam a webapp.
    """

    def __init__(self, get_response):
        """Construtor."""
        self.get_response = get_response

    def __call__(self, request):
        """Executa o middleware."""
        if not settings.DEBUG and not request.is_secure():
            raise http.Http404()

        response = self.get_response(request)
        return response
