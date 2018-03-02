"""Serializadores da aplicação inscritos."""

from rest_framework import serializers

from . import models


class InscritoSerializer(serializers.ModelSerializer):
    """Serializador de inscritos."""

    class Meta:
        """Meta opções do serializador."""

        model = models.Inscrito
        fields = ['email', 'ativo']
        read_only_fields = ['ativo']

    def save(self):
        """Cria um inscrito e envia o email de confirmação."""
        inscrito = models.Inscrito.objects.get_or_create(email=self.validated_data['email'])[0]
        if not inscrito.ativo:
            inscrito.enviar_email_de_confirmação()

        self.instance = inscrito
        return self.instance
