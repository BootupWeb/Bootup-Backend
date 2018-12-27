from rest_framework import serializers

from campaign.models import Detail, Story, Update

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('name', 'category', 'established', 'url', 'demo', 'video', 'location_city', 'location_state', 'progress', 'status', 'phone')

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('details', 'slug', 'product', 'summary', 'pick_project', 'far_along', 'competitors', 'different', 'new', 'money_use', 'user_aquisition',
                  'monetization', 'user_count', 'equity_summary', 'future_six', 'future_one', 'future_two', 'future_three', 'other_projects')

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ('campaign', 'message', 'impact')
