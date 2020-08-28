"""API v1 views for hashtags."""
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tag.api.serializers import HashtagSerializer
from tag.models import Hashtag


class HashtagSearchView(APIView):
    """Search hashtags."""

    def get(self, request, *args, **kwargs):
        """
        Get paginated tag search results.

        <BASE_URL>/<endpoint>/[..query_params]

        Available query_params options:
        1. page_number [int, default 1]
        2. page_size [int, default 50]
        3. search [str]

        misco.com/tags/search/?search=sunny&page_number=3
        """
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
