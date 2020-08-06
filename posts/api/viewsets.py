from rest_framework import viewsets

from posts.api.serializers import *


class PostViewSet(viewsets.ModelViewSet):
    """Post viewset for API."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
