from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from sounds.api.serializers import SoundSerializer
from sounds.controllers.uploader import SoundUploader
from sounds.exceptions import SoundUploadException
from sounds.models import Sound


class SoundUploadView(APIView):
    """Handle sound basic functions."""

    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        """Upload sound to model."""
        if not request.FILES:
            raise SoundUploadException('No Sound file supplied.')
        return Response(
            data=SoundUploader().upload(
                request.user,
                request.FILES,
                request.POST
            ),
            status=status.HTTP_201_CREATED
        )


class SoundSearchView(APIView):
    """Search sounds."""

    def get(self, request, *args, **kwargs):
        """
        Get paginated sound search results.

        <BASE_URL>/<endpoint>/[..query_params]

        Available query_params options:
        1. page_number [int, default 1]
        2. page_size [int, default 50]
        3. search [str] -> maps with the song name

        misco.com/sounds/api/search/?search=zaalima&page_number=1
        """
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
