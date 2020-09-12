"""Utils for activity application."""
from activity.models import PostView, SoundView


def post_views_count(post):
    """Get number of views for the post."""
    return PostView.objects.filter(
        post=post
    ).count()


def sound_views_count(sound):
    """Get number of views for the sound."""
    return SoundView.objects.filter(
        sound=sound
    ).count()
