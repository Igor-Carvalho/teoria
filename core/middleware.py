"""Core middlewares."""

from django import http


class JorgeeWarningMiddleware:
    """todo."""

    def __init__(self, get_response):
        """Construtor."""
        self.get_response = get_response
        self.message = 'This is not a PHP webapp. Stop embarrassing yourself.'

    def __call__(self, request):
        """call."""
        if (
            'jorgee' in request.META.get('HTTP_USER_AGENT', '').lower() or
            'php' in request.path.lower() or
            'pma' in request.path.lower()
        ):
            raise http.Http404()

        response = self.get_response(request)
        return response
