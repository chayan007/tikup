"""Serializers for favorite application."""
from rest_framework.serializers import ModelSerializer

from favorites.models import *

from sounds.api.serializers import SoundSerializer

from posts.api.serializers import PostSerializer

from usermodule.api.serializers import ProfileSerializer


class FavoriteSoundSerializer(ModelSerializer):
    """Serializer for favorite songs."""
    sound = SoundSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = FavoriteSound
        fields = ('sound', 'profile')


class FavoritePostSerializer(ModelSerializer):
    """Serializer for favorite posts."""
    post = PostSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = FavoritePost
        fields = ('post', 'profile')
