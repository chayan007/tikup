"""Common URLs for timeline application."""
from django.urls import path, include

from timeline.api.views import TimelineView

urlpatterns = [
    path('api/', TimelineView.as_view(), name='normal'),
]
