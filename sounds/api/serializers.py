from rest_framework import serializers

from activity.utils import sound_views_count

from favorites.utils import is_sound_favorite

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
    is_favorite = serializers.SerializerMethodField()

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if not request:
            return False
        return is_sound_favorite(
            request.user.profile,
            obj
        )

    def get_views(self, obj):
        return sound_views_count(obj)

    class Meta:
        model = Sound
        fields = (
            'uuid', 'name', 'profile',
            'sound_file', 'first_video', 'copyright',
            'category', 'sound_cover', 'views', 'is_favorite'
        )
