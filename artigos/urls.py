"""Urls da aplicação artigos."""

from django import urls

from . import views

app_name = 'artigos'

urlpatterns = [
    urls.re_path(r'^$', views.artigos_lista, name='lista'),
    urls.re_path(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', views.artigos_detalhe, name='detalhe'),
]
