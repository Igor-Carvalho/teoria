"""URLs da aplicação contato."""

from django import urls

from . import views

app_name = 'contato'

urlpatterns = [
    urls.re_path(r'^$', views.contato, name='contato'),
    urls.re_path(r'^enviar/email/contato/$', views.email_de_contato, name='email_de_contato'),
]
