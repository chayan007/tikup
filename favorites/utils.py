"""Utils for favorites application."""
from activity.models import PostView

from favorites.models import FavoritePost, FavoriteSound


def is_post_favorite(profile, post):
    """Return if post is marked favorite."""
    return FavoritePost.objects.filter(
        post=post,
        profile=profile
    ).exists()


def is_post_viewed(profile, post):
    """Return if post is marked favorite."""
    return PostView.objects.filter(
        post=post,
        profile=profile
    ).exists()


def is_sound_favorite(profile, sound):
    """Return if sound is marked favorite."""
    return FavoriteSound.objects.filter(
        sound=sound,
        profile=profile
    ).exists()
