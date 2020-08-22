"""API v1 views for hashtags."""
from rest_framework.views import APIView


class SoundSearchAPI(APIView):
    """Search tags."""

    def get(self, request, *args, **kwargs):
        """Get paginated search results."""
        page_number = request.query_params.get('page_number ', 1)
        page_size = request.query_params.get('page_size ', 50)
        search_token = request.query_params.get('search', None)
        if not search_token:
            raise Exception('Search Token not provided.')
        posts = Sound.objects.filter(
            name__icontains=search_token
        )
        paginator = Paginator(posts, page_size)
        serializer = SoundSerializer(
            paginator.page(page_number),
            many=True,
            context={'request': request}
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response
