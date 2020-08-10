from rest_framework import viewsets

from sounds.api.serializers import *


class SoundViewSet(viewsets.ModelViewSet):
    """Sound viewset for API."""

    queryset = Sound.objects.all()
    serializer_class = SoundSerializer


class SoundCategoryViewSet(viewsets.ModelViewSet):
    """Sound Category viewset for API."""

    queryset = SoundCategory.objects.all()
    serializer_class = SoundCategorySerializer
