"""Add all API routes."""
from rest_framework import routers

from posts.api.viewsets import PostViewSet


router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)

urls = router.urls
