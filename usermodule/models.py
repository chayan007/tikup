from django.contrib.auth.models import User
from django.db import models

from base.models import BaseModel


class Profile(BaseModel):
    """One-to-one profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    country = models.CharField(max_length=100, null=True)
    is_verified = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    display_pic = models.ImageField(upload_to='user/image/', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class FollowerMap(BaseModel):
    """Follower record database."""

    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return '{} followed {}'.format(
            self.follower.user.username,
            self.following.user.username
        )

    class Meta:
        unique_together = ('follower', 'following',)
