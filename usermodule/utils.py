"""Utility functions for usermodule app."""
from activity.models import Activity

from posts.models import Post

from usermodule.models import FollowerMap


def follower_count(profile_obj):
    """Get no. of followers."""
    return FollowerMap.objects.filter(
        following=profile_obj
    ).count()


def following_count(profile_obj):
    """Get no. of following."""
    return FollowerMap.objects.filter(
        follower=profile_obj
    ).count()


def video_liked_count(profile_obj):
    """Get no. of videos liked."""
    return Activity.objects.filter(
        profile=profile_obj,
        activity_type='L'
    ).count()


def personal_videos_count(profile_obj):
    """Count no. of videos uploaded."""
    return Post.objects.filter(
        profile=profile_obj
    ).count()


def personal_video_like_metric(profile_obj):
    """Get no. of video likes he got."""
    user_posts = Post.objects.filter(
        profile=profile_obj
    )
    return Activity.objects.filter(
        post__in=user_posts,
        activity_type='L'
    ).count()
