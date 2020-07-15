from django.contrib.auth.models import User
from django.db import models

from base.models import BaseModel


class Profile(BaseModel):
    """One-to-one profile model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    country = models.CharField(max_length=100, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()
