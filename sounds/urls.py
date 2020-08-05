"""Common URLs for sounds application."""
from django.urls import path, include

from sounds.api import router


urlpatterns = [
    path('api/models/', include(router.urls)),
]
