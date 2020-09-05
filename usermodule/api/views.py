from django.contrib.auth.models import User
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from usermodule.api.serializers import ProfileSerializer
from usermodule.models import FollowerMap
from usermodule.models import Profile


@api_view(['POST'])
def create_auth(request):
    """
    Create user for Misco.

    request.POST['email']: str
    request.POST['username']: str
    request.POST['password']: password (plain string -> hashing in backend)
    """
    serialized = request.POST
    try:
        user_obj = User.objects.create_user(
            email=serialized['email'],
            username=serialized['username'],
            password=serialized['password']
        )
        Profile.objects.create(user=user_obj)
        return Response({'message': 'User Created !'}, status=status.HTTP_201_CREATED)
    except BaseException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class FollowerRequestView(APIView):
    """Allows one user to follow/unfollow other user."""

    def get(self, request, follow_tag):
        """
        Get list of followers or following.

        Available tag:
        1. follower
        2. following
        """
        if follow_tag.lower() == 'follower':
            uuid_list = FollowerMap.objects.filter(
                following=request.user.profile
            ).values_list(
                'follower__uuid', flat=True
            )
        elif follow_tag.lower() == 'following':
            uuid_list = FollowerMap.objects.filter(
                follower=request.user.profile
            ).values_list(
                'following__uuid', flat=True
            )
        else:
            raise Exception('Proper Tag was not passed.')
        profiles = Profile.objects.filter(
            uuid__in=uuid_list
        )
        serialized = ProfileSerializer(
            profiles,
            many=True
        )
        return Response(
            data=serialized.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, follow_profile_username):
        """Follow an user."""
        following_profile = Profile.objects.get(
            user__username=follow_profile_username
        )
        try:
            FollowerMap.objects.create(
                follower=request.user.profile,
                following=following_profile
            )
            return Response(
                {
                    'message': 'You have followed {}'.format(following_profile.user.get_full_name())
                },
                status=status.HTTP_200_OK
            )
        except BaseException as e:
            FollowerMap.objects.filter(
                follower=request.user.profile,
                following=following_profile
            ).delete()
            return Response(
                {
                    'message': 'You have unfollowed {}'.format(following_profile.user.get_full_name())
                },
                status=status.HTTP_200_OK
            )


class FollowerMetricsView(APIView):
    """Get follower metrics."""

    def get(self, request, follow_tag):
        """
        Get count of followers or following.

        Available follow_tag:
        1. follower
        2. following
        """
        if follow_tag.lower() == 'follower':
            count = FollowerMap.objects.filter(
                following=request.user.profile
            ).count()
        elif follow_tag.lower() == 'following':
            count = FollowerMap.objects.filter(
                follower=request.user.profile
            ).count()
        else:
            raise Exception('Proper Tag was not passed.')
        return Response(
            data={'count': count},
            status=status.HTTP_200_OK
        )


class ProfileSearchView(APIView):
    """Search profiles."""

    def get(self, request, *args, **kwargs):
        """
        Get paginated post search results.

        <BASE_URL>/<endpoint>/[..query_params]

        Available query_params options:
        1. page_number [int, default 1]
        2. page_size [int, default 50]
        3. search [str]

        misco.com/profile/search/?search=martial%20arts&page_size=100
        """
        page_number = request.query_params.get('page_number ', 1)
        page_size = request.query_params.get('page_size ', 100)
        search_token = request.query_params.get('search', None)
        if not search_token:
            raise Exception('Search Token not provided.')
        profiles = Profile.objects.filter(
            user__username__icontains=search_token
        ) | Profile.objects.filter(
            user__first_name=search_token
        ) | Profile.objects.filter(
            user__last_name=search_token
        )
        paginator = Paginator(profiles, page_size)
        serializer = ProfileSerializer(
            paginator.page(page_number),
            many=True,
            context={'request': request}
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response
