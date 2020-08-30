"""API views for favorites."""
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from favorites.api.serializers import *
from favorites.controller.favourite import FavoriteCentral, MarkFavorite


class FavoriteView(APIView):
    """Handle all favorite functions."""

    def post(self, request, model_marker, object_id):
        """
        Mark or unmark a favorite post or sound.

        There are two options for model_marker:
        1. post
        2. sound

        object_id refers to the uuid of the respective model.
        """
        is_favorite_marked = MarkFavorite().mark(
            request.user.profile,
            model_marker,
            object_id
        )
        if is_favorite_marked:
            message = 'Successfully done.'
        else:
            message = 'Unusual Problem was faced.'
        return Response(
            data={'message': message},
            status=status.HTTP_200_OK
        )

    def get(self, request, model_marker):
        """
        Get all favorites for an user.

        There are two options for model_marker:
        1. post
        2. sound

        It will list the favorites based on your model selection.
        """
        page_number = request.query_params.get('page_number ', 1)
        page_size = request.query_params.get('page_size ', 100)
        instances = FavoriteCentral().show(
            request.user.profile,
            model_marker
        )
        if not instances:
            raise Exception('There are no favorites for you to see.')
        paginator = Paginator(instances, page_size)
        serializer = None
        if model_marker.lower() == 'post':
            serializer = FavoritePostSerializer(
                paginator.page(page_number),
                many=True,
                context={'request': request}
            )
        if model_marker.lower() == 'sound':
            serializer = FavoriteSoundSerializer(
                paginator.page(page_number),
                many=True,
                context={'request': request}
            )
        if not serializer:
            return Response(
                data={'error': 'Please pass proper Model marker for favorites retrieval.'},
                status=status.HTTP_417_EXPECTATION_FAILED
            )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
