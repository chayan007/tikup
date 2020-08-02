"""Common URLs for usermodule application."""
from django.urls import path, include

from usermodule.api import router


urlpatterns = [
    path('api/models/', include(router.urls)),
]
