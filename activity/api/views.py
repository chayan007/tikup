"""API views for activity app."""
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from activity.api.serializers import CommentSerializer
from activity.models import Comment


class PostCommentView(APIView):
    """Comment view for every post."""

    permission_classes = (IsAuthenticated, )

    def get(self, request, post_id):
        """Get comment for a single post."""
        comments = Comment.objects.filter(
            post__uuid=post_id
        )
        serialized_comments = CommentSerializer(
            comments, many=True
        ).data
        return Response(
            data=serialized_comments,
            status=status.HTTP_200_OK
        )

    def post(self, request, post_id):
        """Add comment to a post."""
        try:
            Comment.objects.create(
                comment=request.POST['comment'],
                post__uuid=post_id,
                profile=request.user.profile,
                reply=request.POST['reply']
            )
            return Response(
                data={'message': 'Comment Added !'},
                status=status.HTTP_201_CREATED
            )
        except BaseException as e:
            return Response(
                data={'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
