"""URLs da aplicação contato."""

from django.conf import urls

from . import views

app_name = 'contato'

urlpatterns = [
    urls.url(r'^$', views.contato, name='contato'),
    urls.url(r'^enviar/email/contato/$', views.email_de_contato, name='email_de_contato'),
]
