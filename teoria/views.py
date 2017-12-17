"""Global views."""

from django.views import generic

robots = generic.TemplateView.as_view(template_name='robots.txt', content_type='text/plain')

lista_artigos = generic.RedirectView.as_view(permanent=True, pattern_name='artigos:lista')
