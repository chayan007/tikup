"""API views for notifications."""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from notifications.api.serializers import NotificationSerializer
from notifications.controllers.push_notification_strategy import PushNotificationStrategy


class PushNotificationsView(APIView):

    def get(self, request, *args, **kwargs):
        """Get notifications for specific user."""
        notifications = PushNotificationStrategy().get_notifications(request.user.profile)
        serialized_notifications = NotificationSerializer(notifications, many=True)
        return Response(
            data=serialized_notifications.data,
            status=status.HTTP_200_OK
        )