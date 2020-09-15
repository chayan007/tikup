from django.core.paginator import Paginator
from django.db.models import Count
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from sounds.api.serializers import SoundSerializer
from sounds.controllers.converter import AudioConverter
from sounds.controllers.uploader import SoundUploader
from sounds.exceptions import SoundUploadException
from sounds.models import Sound, SoundCategory


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
        sounds = Sound.objects.filter(
            name__icontains=search_token
        )
        paginator = Paginator(sounds, page_size)
        serializer = SoundSerializer(
            paginator.page(page_number),
            many=True,
            context={'request': request}
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response


class SoundCategorySearch(APIView):
    """Get sound based on category."""

    def get(self, request, category_id):
        """Get sounds based on category."""
        page_number = request.query_params.get('page_number ', 1)
        page_size = request.query_params.get('page_size ', 50)
        sounds = Sound.objects.filter(
            category__uuid=category_id
        )
        paginator = Paginator(sounds, page_size)
        serializer = SoundSerializer(
            paginator.page(page_number),
            many=True,
            context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class TrendingSoundCategorisedView(APIView):
    """Get tops songs."""

    def get(self, request, *args, **kwargs):
        """Get top sounds on basis of category."""
        categories = SoundCategory.objects.all()
        response = {}
        for category in categories:
            sounds = Sound.objects.filter(
                category=category
            ).annotate(
                post=Count('post')
            ).order_by('-post')[:10]
            response[category.name] = SoundSerializer(
                sounds,
                many=True,
                context={'request': request}
            )
        return Response(
            data=response,
            status=status.HTTP_200_OK
        )


class SoundExtractorView(APIView):

    def post(self, request, post_uuid):
        """Extract sound of the post."""
        AudioConverter().extract(post_uuid)
        return Response(
            data={'message': 'Sound has been extracted'},
            status=status.HTTP_201_CREATED
        )
