from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from usermodule.api.serializers import UserSerializer


@api_view(['POST'])
def create_auth(request):
    """Create user for Misco."""
    serialized = request.POST
    if serialized.is_valid():
        User.objects.create_user(
            email=serialized.init_data['email'],
            username=serialized.init_data['username'],
            password=serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_profile(request):
    """Create profile for Misco."""
    request_data = request.POST
    username = request_data['username']
