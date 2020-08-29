"""Handle all internal favorite operations."""
from favorites.models import *


class FavoriteCentral:
    """Handle all favorite units."""

    def __init__(self):
        self.profile = ''

    def mark_post(self, post_uuid):
        """Mark or unmark a post."""
        try:
            favorite_post = FavoritePost.objects.filter(
                post=Post.objects.get(uuid=post_uuid),
                profile=self.profile
            )
            if not favorite_post.exists():
                FavoritePost.objects.create(
                    post=Post.objects.get(uuid=post_uuid),
                    profile=self.profile
                )
                return
            favorite_post.delete()
        except BaseException:
            raise Exception('Post was not found.')

    def mark_sound(self, sound_uuid):
        """Mark or unmark a sound."""
        try:
            favorite_sound = FavoriteSound.objects.filter(
                sound=Post.objects.get(uuid=sound_uuid),
                profile=self.profile
            )
            if not favorite_sound.exists():
                FavoriteSound.objects.create(
                    sound=Post.objects.get(uuid=sound_uuid),
                    profile=self.profile
                )
                return
            favorite_sound.delete()
        except BaseException:
            raise Exception('Sound was not found.')

    def mark(self, profile, model_marker, object_uuid):
        """Mark or unmark."""
        self.profile = profile
        if model_marker.lower() == 'post':
            self.mark_post(object_uuid)
            return True
        if model_marker.lower() == 'sound':
            self.mark_sound(object_uuid)
            return True
        return False

