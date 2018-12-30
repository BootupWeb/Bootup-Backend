from rest_framework import serializers

from chat.models import Chat, Message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('campaign', 'investor', 'subject')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('chat', 'founder', 'message', 'media', 'link', 'status')
