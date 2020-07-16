from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel

from usermodule.models import Profile


class Notification(BaseModel):
    """Store notifications for user."""

    class NotificationCategory(models.IntegerChoices):
        """Notification category choices."""
        MAIL = 1, _('Mail')
        PUSH = 2, _('Push')
        SMS = 3, _('SMS')
        CALL = 4, _('Call')
        OTHER = 0, _('Other')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.BooleanField(default=False)
    category = models.IntegerField(choices=NotificationCategory.choices, default=NotificationCategory.OTHER)

    def __str__(self):
        return '{} notified through {}'.format(
            self.profile.user.get_full_name(),
            self.get_category_display()
        )
