from django.db import models

from base.models import BaseModel

from posts.models import Post


class Hashtag(BaseModel):
    """Model for hashtags."""

    name = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HashtagLink(BaseModel):
    """Model for hashtags mapping with post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)

    def __str__(self):
        """ Harish Ugniv -> Yolo : Representation layer."""
        return '{} -> {}'.format(
            self.post.profile.user.get_full_name(),
            self.hashtag.name
        )
