from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from sounds.controllers.uploader import SoundUploader
from sounds.exceptions import SoundUploadException


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
