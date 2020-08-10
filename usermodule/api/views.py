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
        user_obj = User.objects.create_user(
            email=serialized['email'],
            username=serialized['username'],
            password=serialized['password']
        )
        Profile.objects.create(user=user_obj)
        return Response({'message': 'User Created !'}, status=status.HTTP_201_CREATED)
    except BaseException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
