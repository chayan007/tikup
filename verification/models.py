from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel

from usermodule.models import Profile


class OTP(BaseModel):
    """Model to support OTP Verification."""

    class OTPReasons(models.IntegerChoices):
        """Choices for ownership."""
        ACCOUNT_ACTIVATION = 0, _('Account Activation')
        CELEBRITY_VERIFICATION = 1, _('Celebrity Verification')
        PASSWORD_RESET = 2, _('Password Reset')
        UNUSUAL_ACTIVITY = 3, _('Unusual Activity')
        OTHER = 4, _('Other')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    verified_at = models.DateTimeField(null=True, blank=True)
    reason = models.IntegerField(null=True, choices=OTPReasons.choices, default=OTPReasons.OTHER.value)

    def __str__(self):
        return '{} -> {}'.format(self.profile.user.first_name, self.reason)
