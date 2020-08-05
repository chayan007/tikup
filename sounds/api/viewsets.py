from rest_framework import viewsets

from sounds.api.serializers import *


class SoundViewSet(viewsets.ModelViewSet):
    """Sound viewset for API."""

    queryset = Sound.objects.all()
    serializer_class = SoundSerializer
