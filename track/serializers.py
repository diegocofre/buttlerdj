from rest_framework import serializers
from track.models import Track, Segment, Milestone

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'name', 'short_description', 'long_description','segments']

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ['id', 'name', 'short_description', 'long_description','duration','duration_tunit','end_message','end_confirm','milestones']

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['id', 'name', 'short_description', 'long_description','happens_at','happens_at_tunit','periodicity','periodicity_tunit']
