from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import Credential, Profile, Founder
from .serializers import CredentialSerializer, ProfileSerializer, FounderSerializer

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


class FounderListView(ListAPIView):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer

class FounderDetailsView(RetrieveAPIView):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer
