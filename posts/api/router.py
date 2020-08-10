"""Add all API routes."""
from rest_framework import routers

from posts.api.viewsets import PostCategoryViewSet, PostViewSet


router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'post-categories', PostCategoryViewSet)

urls = router.urls
