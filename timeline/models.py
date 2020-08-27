from django.db import models

from base.models import BaseModel
from posts.models import Post
from usermodule.models import Profile


class SeenPost(BaseModel):
    """Mark all posts seen by the user."""

    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)

    def __str__(self):
        return '{} has seen {}'.format(
            self.profile.user.get_full_name(),
            self.post.description[:20]
        )
