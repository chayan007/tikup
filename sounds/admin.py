from django.contrib import admin

from sounds.models import Sound
from sounds.utils import *


@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    """Admin for sound model."""

    def get_profile_photo_url(self, obj):
        return profile_photo_url(obj)

    def get_video_count(self, obj):
        return video_count(obj)

    list_display = (
        'name', 'profile', 'first_video',
        'get_profile_photo_url',
        'get_video_count'
    )
