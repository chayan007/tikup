from rest_framework import serializers

from activity.utils import sound_views_count
from usermodule.api.serializers import ProfileSerializer

from sounds.models import Sound, SoundCategory


class SoundCategorySerializer(serializers.ModelSerializer):
    """Serializer for sound category model."""

    class Meta:
        model = SoundCategory
        fields = ('uuid', 'name', 'icon', 'description')


class SoundSerializer(serializers.ModelSerializer):
    """Serializer for sound model."""
    profile = ProfileSerializer()
    category = SoundCategorySerializer()
    views = serializers.SerializerMethodField()

    def get_views(self, obj):
        return sound_views_count(obj)

    class Meta:
        model = Sound
        fields = (
            'uuid', 'name', 'profile',
            'sound_file', 'first_video', 'copyright',
            'category', 'sound_cover', 'views'
        )
