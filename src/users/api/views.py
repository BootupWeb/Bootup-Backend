from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import Credentials
from .serializers import CredentialsSerializer


class CredentialListView(ListAPIView):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer


class CredentialDetailsView(RetrieveAPIView):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer
