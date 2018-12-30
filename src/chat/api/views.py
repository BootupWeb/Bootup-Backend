from rest_framework.generics import ListAPIView, RetrieveAPIView

from chat.models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetailsView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetailsView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
