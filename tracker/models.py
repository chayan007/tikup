from django.db import models

from base.models import BaseModel


class PostLocation(BaseModel):
    """Store location of posts."""

    ip_address = models.GenericIPAddressField()
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.ip_address
