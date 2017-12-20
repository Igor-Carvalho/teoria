"""Serializadores da aplicação contato."""

from django.conf import settings
from post_office import mail
from rest_framework import serializers


class EmailDeContatoSerializer(serializers.Serializer):
    """Serializador para o email de contato."""

    nome = serializers.CharField()
    email = serializers.EmailField()
    website = serializers.URLField(default='Não informado')
    local = serializers.CharField(default='Não informado')
    assunto = serializers.CharField()
    mensagem = serializers.CharField()

    def save(self, **kwargs):
        """Envia a mensagem de email."""
        campos = self.validated_data
        mensagem = '{nome} de {local} do site {website} disse: <br/><br/>'.format(**campos)
        mensagem += campos['mensagem']

        mail.send(
            settings.OWNER_EMAIL,
            campos['email'],
            subject=campos['assunto'],
            html_message=mensagem,
            priority='now'
        )
