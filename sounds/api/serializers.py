from rest_framework import serializers

from usermodule.api.serializers import ProfileSerializer

from sounds.models import Sound, SoundCategory


class SoundCategorySerializer(serializers.ModelSerializer):
    """Serializer for sound category model."""

    class Meta:
        model = SoundCategory
        fields = ('name', 'icon', 'description')


class SoundSerializer(serializers.ModelSerializer):
    """Serializer for sound model."""
    profile = ProfileSerializer()
    category = SoundCategorySerializer()

    class Meta:
        model = Sound
        fields = ('name', 'profile', 'sound_file', 'first_video', 'copyright', 'category')
