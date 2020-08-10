from django.db import models

from base.models import BaseModel

from usermodule.models import Profile


class Copyright(BaseModel):
    """Model to store all copyright."""

    name = models.CharField(max_length=300)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SoundCategory(BaseModel):
    """Model to store all copyright."""

    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Sound(BaseModel):
    """Model to store all sounds."""

    name = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sound_file = models.FileField(upload_to='uploads/sounds/')
    first_video = models.FileField(upload_to='uploads/videos/', null=True, blank=True)
    copyright = models.ForeignKey(Copyright, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(SoundCategory, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
