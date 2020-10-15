from rest_framework import serializers

from usermodule.models import *
from usermodule.utils import get_profile_metrics


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for User."""

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer class for Profile."""
    user = UserSerializer()
    metrics = serializers.SerializerMethodField()

    def get_metrics(self, obj):
        """Get profile metrics."""
        return get_profile_metrics(obj)

    class Meta:
        model = Profile
        fields = ('uuid', 'user', 'dob', 'country',
                  'is_verified', 'is_private',
                  'display_pic', 'metrics')
