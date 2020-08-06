from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.controllers.uploader import PostUploader
from posts.exceptions import PostUploadException


class PostUploadView(APIView):
    """Handle post basic functions."""

    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        """Upload post to model."""
        if not request.FILES:
            raise PostUploadException('No Video file supplied.')
        return Response(
            data=PostUploader().upload(
                request.user,
                request.FILES,
                request.POST
            ),
            status=status.HTTP_201_CREATED
        )
