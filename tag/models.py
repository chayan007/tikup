from django.db import models


class Hashtag(models.Model):
    """Model for hashtags."""

    name = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HashtagLink(models.Model):
    """Model for hashtags mapping with post."""

    post = 1
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)