"""Utility functions ofr Pospost."""
from activity.models import Activity

from posts.models import Post


def likes_count(post_obj):
    """Return likes count."""
    return Activity.objects.filter(
        post=post_obj
    ).count()


def comments_count(post_obj):
    """Return comments count."""
    return Activity.objects.filter(
        post=post_obj
    ).count()


def share_count(post_obj):
    """Return share count."""
    return Post.objects.filter(
        share_pointer=post_obj
    ).count()


def original_creator(post_obj):
    """Return first creator of the post used if shared."""
    return post_obj.share_pointer.profile
