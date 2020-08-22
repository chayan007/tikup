"""API v1 views for hashtags."""
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tag.api.serializers import HashtagSerializer
from tag.models import Hashtag


class SoundSearchAPI(APIView):
    """Search tags."""

    def get(self, request, *args, **kwargs):
        """Get paginated search results."""
        page_number = request.query_params.get('page_number ', 1)
        page_size = request.query_params.get('page_size ', 50)
        search_token = request.query_params.get('search', None)
        if not search_token:
            raise Exception('Search Token not provided.')
        posts = Hashtag.objects.filter(
            name__icontains=search_token
        ).order_by('views')
        paginator = Paginator(posts, page_size)
        serializer = HashtagSerializer(
            paginator.page(page_number),
            many=True,
            context={'request': request}
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response
