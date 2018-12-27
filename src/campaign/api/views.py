from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import DetailSerializer, StorySerializer, UpdateSerializer
from campaign.models import Detail, Story, Update

class DetailListView(ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class DetailDetailsView(RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class StoryListView(ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class StoryDetailsView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class UpdateListView(ListAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

class UpdateDetailsView(RetrieveAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
