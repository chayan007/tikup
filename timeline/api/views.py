"""Add global level timeline APIs."""
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.api.serializers import PostSerializer
from timeline.controllers.central import TimelineCentral


class TimelineView(APIView):
    """Display timeline for authenticated user."""

    def get(self, request, *args, **kwargs):
        """Get the paginated timeline for authenticated user."""
        page_number = request.query_params.get('page_number ', 1)
        page_size = request.query_params.get('page_size ', 100)
        posts = TimelineCentral().posts(request)
        if not posts:
            raise Exception('There are no posts for you to see.')
        paginator = Paginator(posts, page_size)
        serializer = PostSerializer(
            paginator.page(page_number),
            many=True,
            context={'request': request}
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
