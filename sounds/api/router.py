"""Add all API routes."""
from rest_framework import routers

from sounds.api.viewsets import SoundCategoryViewSet, SoundViewSet


router = routers.DefaultRouter()

router.register(r'sounds', SoundViewSet)
router.register(r'sound-categories', SoundCategoryViewSet)

urls = router.urls
