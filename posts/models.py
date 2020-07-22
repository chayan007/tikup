from django.db import models

from base.models import BaseModel

from sounds.models import Sound

from usermodule.models import Profile


class Post(BaseModel):
    """Model for posts."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sound = models.ForeignKey(Sound, on_delete=models.PROTECT)
    video_file = models.FileField(upload_to='uploads/videos/')
    video_gif = models.FileField(upload_to='uploads/gifs/')
    description = models.TextField(null=True)

    def __str__(self):
        return self.profile.user.get_full_name()
