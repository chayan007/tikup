from rest_framework import viewsets

from usermodule.api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """User viewset for API."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """Profile viewset for API."""

    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
