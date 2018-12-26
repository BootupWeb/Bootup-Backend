from rest_framework import serializers

from users.models import Credential, Profile, Role

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ('username', 'email', 'password', 'token')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'gender', 'phone', 'city', 'state', 'day', 'month', 'year', 'website')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('user', 'type', 'company', 'position', 'commitment', 'since_month', 'since_year', 'portfolio', 'verified')
