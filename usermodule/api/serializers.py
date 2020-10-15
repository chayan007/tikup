from rest_framework import serializers

from usermodule.models import *
from usermodule.utils import get_profile_metrics, is_followed


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for User."""

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer class for Profile."""
    user = UserSerializer()
    metrics = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()

    def get_is_followed(self, obj):
        """Get if profile is followed or not."""
        request = self.context.get('request')
        if not request:
            return False
        return is_followed(
            request.user.profile,
            obj
        )

    def get_metrics(self, obj):
        """Get profile metrics."""
        return get_profile_metrics(obj)

    class Meta:
        model = Profile
        fields = ('uuid', 'user', 'dob', 'country',
                  'is_verified', 'is_private',
                  'display_pic', 'metrics', 'is_followed')
