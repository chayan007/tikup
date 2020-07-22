from django.db import models

from base.models import BaseModel

from posts.models import Post

from usermodule.models import Profile


class Activity(BaseModel):
    """Model to record user interactions with applications."""
    FAVORITE = 'F'
    LIKE = 'L'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} -> {}'.format(
            self.profile.user.get_full_name(),
            self.get_activity_type_display()
        )
