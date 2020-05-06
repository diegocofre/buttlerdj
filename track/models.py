from django.db import models
import uuid

TIME_UNITS = [
  ("D", "Day"),
  ("H", "Hour"),
  ("M", "Wednesday")
]

# Create your models here.
class BaseModel():
    created_at = models.DateTimeField(
        auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Meta:
    abstract = True


class Track(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=128)
    long_description = models.CharField(max_length=4086)


class Segment(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_track = models.ForeignKey(
        "track.Track", verbose_name="", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=128)
    long_description = models.CharField(max_length=4086)
    duration = models.IntegerField(null=True, blank=True)
    duration_tunit = models.CharField(
        choices=TIME_UNITS, null=True, blank=True,max_length=1)
    end_message = models.CharField(null=True, blank=True, max_length=128)
    end_confirm = models.BooleanField()



class Milestone(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_segment = models.ForeignKey(
        "track.Segment", verbose_name="", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=128)
    long_description = models.CharField(max_length=4086)
    happens_at = models.IntegerField(default=0)
    happens_at_tunit = models.CharField(
        choices=TIME_UNITS, default="M", max_length=1)
    periodicity = models.IntegerField(null=True, blank=True)
    periodicity_tunit = models.CharField(
        choices=TIME_UNITS, null=True, blank=True,max_length=1)
