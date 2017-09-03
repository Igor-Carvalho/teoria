"""Views da aplicação contato."""

from django.views import generic
from rest_framework import generics

from . import serializers


class ContatoView(generic.TemplateView):
    """Formulário de contato."""

    template_name = 'contato/contato.html'


contato = ContatoView.as_view()


class EmailDeContatoView(generics.CreateAPIView):
    """Endpoint para o envio de mensagens de email."""

    serializer_class = serializers.EmailDeContatoSerializer


email_de_contato = EmailDeContatoView.as_view()
