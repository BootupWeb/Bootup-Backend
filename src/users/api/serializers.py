from rest_framework import serializers

from django.contrib.auth.models import User
from users.models import Profile, Role

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'last_login')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'city', 'state', 'phone', 'gender', 'day', 'month', 'year', 'website', 'type')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('user', 'profile', 'campaign', 'firm', 'position', 'summary', 'since_month', 'since_year', 'current_inv', 'top_inv', 'verified')
