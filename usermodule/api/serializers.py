from rest_framework import serializers

from usermodule.models import *


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for User."""

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer class for Profile."""
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('uuid', 'user', 'dob', 'country',
                  'is_verified', 'is_private',
                  'display_pic')
