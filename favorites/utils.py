"""Utils for favorites application."""
from favorites.models import FavoritePost, FavoriteSound


def is_post_favorite(profile, post):
    """Return if post is marked favorite."""
    return FavoritePost.objects.filter(
        post=post,
        profile=profile
    ).exist()


def is_sound_favorite(profile, sound):
    """Return if sound is marked favorite."""
    return FavoriteSound.objects.filter(
        sound=sound,
        profile=profile
    ).exist()
