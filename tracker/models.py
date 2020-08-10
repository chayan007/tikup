from django.db import models

from base.models import BaseModel


class PostLocation(BaseModel):
    """Store location of posts."""

    ip_address = models.GenericIPAddressField()
    state = models.CharField(null=True, blank=True)
    country = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.ip_address