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
    icon = models.ImageField(upload_to='system/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Sound(BaseModel):
    """Model to store all sounds."""

    name = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cover_pic = models.ImageField(upload_to='uploads/sounds_covers/', null=True, blank=True)
    sound_file = models.FileField(upload_to='uploads/sounds/')
    sound_cover = models.FileField(upload_to='uploads/cover/', null=True, blank=True)
    first_video = models.FileField(upload_to='uploads/videos/', null=True, blank=True)
    copyright = models.ForeignKey(Copyright, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(SoundCategory, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
