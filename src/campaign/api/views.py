from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import DetailSerializer
from campaign.models import Detail

class DetailListView(ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class DetailDetailsView(RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
