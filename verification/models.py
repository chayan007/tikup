from django.db import models

from base.models import BaseModel

from usermodule.models import Profile


class OTP(BaseModel):
    """Model to support OTP Verification."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    verified_at = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{} -> {}'.format(self.profile.user.first_name, self.reason)
