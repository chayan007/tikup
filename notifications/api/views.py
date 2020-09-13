"""API views for notifications."""
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from notifications.api.serializers import NotificationSerializer
from notifications.controllers.push_notification_strategy import PushNotificationStrategy


class PushNotificationsView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        """Get notifications for specific user."""
        notifications = PushNotificationStrategy().get_notifications(request.user.profile)
        serialized_notifications = NotificationSerializer(notifications, many=True)
        return Response(
            data=serialized_notifications.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Mark all notifications read.

        request.POST['notification_uuids'] : [str, str, str]
            eg: ['sd034bf-1237sb9s-asfb2341', 'bcd125-gf433s-cer521']
        """
        PushNotificationStrategy().mark_notifications(
            request.data['notification_uuids']
        )
        return Response(
            data={'message': 'All notifications are marked read !'}
        )
