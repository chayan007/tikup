from rest_framework import viewsets

from posts.api.serializers import *


class PostViewSet(viewsets.ModelViewSet):
    """Post viewset for API."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCategoryViewSet(viewsets.ModelViewSet):
    """Post Category viewset for API."""

    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer

