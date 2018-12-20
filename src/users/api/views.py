from rest_frameworks.generics import ListAPIView

from users.models import Credentials
from .sereializers import CredentialsSerializer


class CredentialListView(ListAPIView):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer


class CredentialDetailsView(RetrieveAPIView):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer
