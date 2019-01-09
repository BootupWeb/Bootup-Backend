from rest_framework import serializers

from campaign.models import Detail, Story, Update

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('name', 'slug', 'category', 'established', 'url', 'video', 'location_city', 'location_state', 'progress', 'status', 'equity', 'amount',
                    'valuation', 'features_image')

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('details', 'product', 'pick_project', 'far_along', 'competitors', 'different', 'new', 'money_use', 'user_aquisition',
                  'monetization', 'user_count', 'future_six', 'future_one', 'future_two', 'future_three', 'other_projects')

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ('campaign', 'message')
