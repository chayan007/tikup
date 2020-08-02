"""Add all API routes."""
from rest_framework import routers

from usermodule.api.viewsets import ProfileViewSet, UserViewSet


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urls = router.urls
