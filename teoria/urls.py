"""Módulo de configuração de urls do projeto."""

from django.conf import settings, urls
from django.conf.urls import static
from django.contrib import admin

from . import routes, views

urlpatterns = [
    urls.url(r'^$', views.lista_artigos),
    urls.url(r'^robots\.txt$', views.robots, name='robots.txt'),
    urls.url(r'^artigos/', urls.include('artigos.urls', namespace='artigos')),
    urls.url(r'^contatos/', urls.include('contato.urls', namespace='contato')),
    urls.url(r'^administração/', urls.include(admin.site.urls)),
    urls.url(r'^api/v1/', urls.include(routes.urls, namespace='v1')),
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        urls.url(r'^__debug__/', urls.include(debug_toolbar.urls))
    ]
