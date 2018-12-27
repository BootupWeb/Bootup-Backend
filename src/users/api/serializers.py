from rest_framework import serializers

from users.models import Credential, Profile, Founder

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ('username', 'email', 'password', 'token')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'gender', 'phone', 'city', 'state', 'day', 'month', 'year', 'website')

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = ('user', 'campaign', 'company', 'position', 'commitment', 'since_month', 'since_year', 'portfolio', 'verified')
