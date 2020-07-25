from django.contrib import admin

from usermodule.models import Profile
from usermodule.utils import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin for profile model."""

    def get_follower_count(self, obj):
        return follower_count(obj)

    def get_following_count(self, obj):
        return following_count(obj)

    def get_video_liked_count(self, obj):
        return video_liked_count(obj)

    def get_personal_videos_count(self, obj):
        return personal_videos_count(obj)

    def get_personal_video_like_metric(self, obj):
        return personal_video_like_metric(obj)

    list_display = (
        'user', 'country', 'is_private',
        'get_follower_count', 'get_following_count',
        'get_video_liked_count', 'get_personal_video_like_metric',
        'get_personal_videos_count'
    )
