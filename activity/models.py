from django.db import models

from base.models import BaseModel

from posts.models import Post

from usermodule.models import Profile


class Activity(BaseModel):
    """Model to record user interactions with applications."""
    FAVORITE = 'F'
    LIKE = 'L'
    REPORT = 'R'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (REPORT, 'Report')
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} -> {}'.format(
            self.profile.user.get_full_name(),
            self.get_activity_type_display()
        )

    class Meta:
        unique_together = ('profile', 'post', 'activity_type',)


class Comment(BaseModel):
    """Store comments for posts."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return '{}: {}'.format(
            self.profile.user.get_full_name(),
            self.comment[:100]
        )