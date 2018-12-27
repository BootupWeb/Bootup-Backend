from rest_framework import serializers

from campaign.models import Detail

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('name', 'category', 'sub_category', 'established', 'url', 'demo', 'video', 'location_city', 'location_state', 'progress', 'status', 'phone')
