from django.core.paginator import Paginator
from django.db.models import Count

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.api.serializers import PostSerializer
from posts.controllers.uploader import PostUploader
from posts.exceptions import PostUploadException
from posts.models import Post
from posts.utils import comments_count, likes_count, share_count

from tag.models import Hashtag, HashtagLink


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
                request.POST,
                request
            ),
            status=status.HTTP_201_CREATED
        )


class PostSearchView(APIView):
    """Search posts."""

    def get(self, request, *args, **kwargs):
        """
        Get paginated post search results.

        <BASE_URL>/<endpoint>/[..query_params]

        Available query_params options:
        1. page_number [int, default 1]
        2. page_size [int, default 50]
        3. search [str]

        misco.com/post/search/?search=martial%20arts&page_size=100
        """
        page_number = request.query_params.get('page_number', 1)
        page_size = request.query_params.get('page_size', 50)
        search_token = request.query_params.get('search', None)
        if not search_token:
            raise Exception('Search Token not provided.')
        posts = Post.objects.filter(
            description__icontains=search_token
        ).exclude(
            is_pornographic=True
        )
        paginator = Paginator(posts, page_size)
        serializer = PostSerializer(
            paginator.page(page_number),
            many=True,
            context={'request': request}
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response


class PostMetricsView(APIView):
    """Get all post metrics."""

    def get(self, request, indicator, post_id):
        """
        Get post metrics based on the indicator passed.

        Types of indicators available:
        1. likes
        2. comments
        3. shares

        The count of the indicator will be returned.
        """
        indicator = indicator.lower()
        post = Post.objects.get(uuid=post_id)
        if indicator == 'likes':
            count = likes_count(post)
        elif indicator == 'comments':
            count = comments_count(post)
        elif indicator == 'shares':
            count = share_count(post)
        else:
            return Response(
                data={'error': 'Proper indicator is not supplied.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            data={'count': count},
            status=status.HTTP_200_OK
        )


class SoundBasedPostView(APIView):
    """Return all posts by same sound."""

    def get(self, request, sound_id):
        """Return all posts by same sound."""
        posts = Post.objects.filter(
            sound__uuid=sound_id
        ).annotate(
            num_likes=Count('activity')
        ).order_by('-num_likes')[:100]
        serializer = PostSerializer(
            posts,
            many=True
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class UserPostView(APIView):
    """Get all post by the user."""

    def get(self, request, username):
        """Get all videos for a profile."""
        posts = Post.objects.filter(
            profile__user__username=username
        )
        serialized = PostSerializer(
            posts,
            many=True
        )
        return Response(
            data=serialized.data,
            status=status.HTTP_200_OK
        )


class UserLikedPostView(APIView):
    """Get the posts interacted by user."""

    def get(self, request, username):
        """Get all posts liked by the user."""
        posts = Post.objects.filter(
            profile__user__username=username
        ).annotate(
            num_likes=Count('activity')
        ).order_by('-created_at')
        serialized = PostSerializer(
            posts,
            many=True
        )
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )


class TrendingTagPostView(APIView):
    """Display all trending posts based on tags."""

    def get(self, request, *args, **kwargs):
        """Get all trending posts based on tags."""
        popular_hashtags = Hashtag.objects.all().order_by('-count')[:20]
        response = {}
        for hashtag in popular_hashtags:
            posts = Post.objects.filter(
                uuid__in=HashtagLink.objects.filter(
                    hashtag=hashtag
                ).values_list(
                    'post__uuid', flat=True
                )
            ).annotate(
                num_likes=Count('activity')
            ).order_by('-num_likes')[:10]
            response[hashtag.name] = PostSerializer(
                posts,
                many=True
            ).data
        return Response(
            data=response,
            status=status.HTTP_200_OK
        )
