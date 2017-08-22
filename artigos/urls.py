"""Urls da aplicação artigos."""

from django.conf import urls

from . import views

app_name = 'artigos'

urlpatterns = [
    urls.url(r'^$', views.artigos_lista, name='lista'),
    urls.url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', views.artigos_detalhe, name='detalhe'),
]
