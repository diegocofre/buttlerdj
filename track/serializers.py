from rest_framework import serializers
from track.models import Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'name', 'short_description', 'long_description']