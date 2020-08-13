"""Serializers for Notifications."""
from rest_framework.serializers import ModelSerializer

from notifications.models import Notification

from usermodule.api.serializers import ProfileSerializer


class NotificationSerializer(ModelSerializer):
    """Serializer class for notification."""
    profile = ProfileSerializer()

    class Meta:
        model = Notification
        fields = ('profile', 'message', 'status', 'category')
