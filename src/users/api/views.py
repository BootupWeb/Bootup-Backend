from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import Credential, Profile, Role
from .serializers import CredentialSerializer, ProfileSerializer, RoleSerializer

class CredentialListView(ListAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

class CredentialDetailsView(RetrieveAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer


class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailsView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetailsView(RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
