"""Serializers for tag model."""
from rest_framework.serializers import ModelSerializer

from tag.models import Hashtag


class HashtagSerializer(ModelSerializer):
    """Tag serializer model class."""

    class Meta:
        model = Hashtag
        fields = ('name', 'views')
