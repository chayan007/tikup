"""Common URLs for notification application."""
from django.urls import path

from notifications.api.views import PushNotificationsView

urlpatterns = [
    path('api/push/', PushNotificationsView.as_view(), name='push')
]
