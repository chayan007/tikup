from django.contrib import admin

from sounds.models import Copyright, Sound, SoundCategory
from sounds.utils import *


@admin.register(Copyright)
class CopyrightAdmin(admin.ModelAdmin):
    """Admin for copyright."""

    list_display = ('name', 'is_verified', )


@admin.register(SoundCategory)
class SoundCategoryAdmin(admin.ModelAdmin):
    """Admin for sound Category."""

    list_display = ('name', 'icon', 'description')


@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    """Admin for sound model."""

    def get_profile_photo_url(self, obj):
        return profile_photo_url(obj)

    def get_video_count(self, obj):
        return video_count(obj)

    list_display = (
        'name', 'profile', 'category', 'sound_file',
        'get_profile_photo_url',
        'get_video_count'
    )
