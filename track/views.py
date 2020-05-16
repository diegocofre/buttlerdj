import logging
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from track.models import Track, Segment, Milestone
from track.serializers import TrackSerializer, SegmentSerializer, MilestoneSerializer
from rest_framework import generics

logger = logging.getLogger(__name__)


def index(request):
    try:
        return render(request, "index.html", None)
    except:
        logger.exception('')


def shoot(request, name):
    r = None

    try:
        raise Exception('Log my raised ex')
    except Exception as e:
        r = str(e)
        logger.exception('')

    r = "name = {0} -  ex: {1}".format(name, r)
    return HttpResponse(r)


class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class SegmentList(generics.ListCreateAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


class SegmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


class MilestoneList(generics.ListCreateAPIView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer


class MilestoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
