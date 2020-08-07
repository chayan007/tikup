from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from usermodule.models import Profile


@api_view(['POST'])
def create_auth(request):
    """Create user for Misco."""
    serialized = request.POST
    try:
        User.objects.create_user(
            email=serialized['email'],
            username=serialized['username'],
            password=serialized['password']
        )
        return Response({'message': 'User Created !'}, status=status.HTTP_201_CREATED)
    except BaseException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_profile(request):
    """Create profile for Misco."""
    request_data = request.POST
    try:
        Profile.objects.create(
            user__username=request_data['username']
        )
        return Response({
            'message': 'Profile Created for {}!'.format(request_data['username'])
        }, status=status.HTTP_201_CREATED)
    except BaseException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
