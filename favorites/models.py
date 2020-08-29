from django.db import models

from base.models import BaseModel

from posts.models import Post

from sounds.models import Sound

from usermodule.models import Profile


class FavoriteSound(BaseModel):
    """Mark all favorite songs of an user."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sound = models.ForeignKey(Sound, on_delete=models.CASCADE)

    def __str__(self):
        """Representation."""
        return '{} has marked {} as favorite'.format(
            self.profile.user.username,
            self.sound.name
        )


class FavoritePost(BaseModel):
    """Mark all favorite posts of an user."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        """Representation."""
        return '{} has marked {} as favorite'.format(
            self.profile.user.username,
            self.post.description[:20]
        )
