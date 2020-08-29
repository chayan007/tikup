"""Add global level timeline APIs."""
from rest_framework.views import APIView

from posts.models import Post


class TimelineView(APIView):
    """Display timeline for authenticated user."""

    def get(self, request, *args, **kwargs):
        """Get the paginated timeline for authenticated user."""
        page_number = request.query_params.get('page_number ', 1)
        page_size = request.query_params.get('page_size ', 50)
        posts = Post.objects.filter(
            is_pornographic=False,
            uploaded_location__country=
        )