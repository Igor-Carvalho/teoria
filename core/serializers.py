"""Serializadores da aplicação core."""

from django.contrib import auth
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    class Meta:
        """Model Meta."""

        model = auth.get_user_model()
        fields = ['id', 'username']
