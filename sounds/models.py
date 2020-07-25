from django.db import models

from base.models import BaseModel

from usermodule.models import Profile


class Sound(BaseModel):
    """Model to store all sounds."""

    name = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sound_file = models.FileField(upload_to='uploads/sounds/')
    first_video = models.FileField(upload_to='uploads/videos/', null=True, blank=True)

    def __str__(self):
        return self.name
