"""Módulo de configuração de urls do projeto."""

from django import urls
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin

from . import api, views

urlpatterns = [
    urls.re_path(r'^$', views.lista_artigos),
    urls.re_path(r'^robots\.txt$', views.robots, name='robots.txt'),
    urls.re_path(r'^artigos/', urls.include('artigos.urls', namespace='artigos')),
    urls.re_path(r'^contatos/', urls.include('contato.urls', namespace='contato')),
    urls.re_path(r'^administração/', admin.site.urls),
    urls.re_path(r'^api/v1/', api.urls),
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        urls.re_path(r'^__debug__/', urls.include(debug_toolbar.urls))
    ]
