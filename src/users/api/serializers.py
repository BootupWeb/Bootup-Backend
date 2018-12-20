from rest_framework import serializers

from users.models import Credentials


class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = ('username', 'email', 'password')
