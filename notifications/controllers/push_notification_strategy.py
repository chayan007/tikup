from notifications.models import Notification


class PushNotificationCentral:

    PUSH_CONSTANT = 2

    def get_notifications(self, profile):
        """Get all notifications for a profile."""
        return Notification.objects.filter(
            profile=profile,
            category=self.PUSH_CONSTANT
        ).order_by('-created_at')[:50]

    def mark_notifications(self, notification_uuids):
        """Marks notifications read."""
        for notification_uuid in notification_uuids:
            notification = Notification.objects.get(
                uuid=notification_uuid
            )
            notification.status = True
            notification.save()