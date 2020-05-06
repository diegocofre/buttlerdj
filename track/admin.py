from django.contrib import admin

# Register your models here.
from .models import Track, Segment, Milestone
admin.site.register(Track)
admin.site.register(Segment)
admin.site.register(Milestone)
