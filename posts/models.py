from django.db import models

from base.models import BaseModel

from sounds.models import Sound

from usermodule.models import Profile


class PostCategory(BaseModel):
    """Model to store all copyright."""

    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Post(BaseModel):
    """Model for posts."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sound = models.ForeignKey(Sound, on_delete=models.PROTECT)
    video_file = models.FileField(upload_to='uploads/videos/')
    video_gif = models.FileField(upload_to='uploads/gifs/', null=True, blank=True)
    description = models.TextField(null=True)
    share_pointer = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    category = models.ForeignKey(PostCategory, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.profile.user.get_full_name()
