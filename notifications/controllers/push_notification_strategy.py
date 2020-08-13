from notifications.models import Notification


class PushNotificationStrategy:

    PUSH_CONSTANT = 2

    def get_notifications(self, profile):
        """Get all notifications for a profile."""
        return Notification.objects.filter(
            profile=profile,
            category=self.PUSH_CONSTANT
        ).order_by('-created_at')

    def mark_notifications(self, notification_uuids):
        """Marks notifications read."""
        for notification_uuid in notification_uuids:
            notification = Notification.objects.get(
                uuid=notification_uuid,
                category=self.PUSH_CONSTANT
            )
            notification.status = True
            notification.save()

    def create_notifications(self, profile, message):
        """Create notification for user."""
        Notification.objects.create(
            profile=profile,
            message=message,
            category=self.PUSH_CONSTANT
        )
