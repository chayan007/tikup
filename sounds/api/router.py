"""Add all API routes."""
from rest_framework import routers

from sounds.api.viewsets import SoundViewSet


router = routers.DefaultRouter()

router.register(r'sounds', SoundViewSet)

urls = router.urls
