from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from activity.models import Activity

from base.models import BaseModel

from sounds.models import Sound

from usermodule.models import Profile


class Post(BaseModel):
    """Model for posts."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sound = models.ForeignKey(Sound, on_delete=models.PROTECT)
    video_file = models.FileField(upload_to='uploads/video/')
    description = models.TextField(null=True)
    likes = GenericRelation(Activity)

    def __str__(self):
        return self.profile.user.get_full_name()
