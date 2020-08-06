from rest_framework import serializers

from usermodule.api.serializers import ProfileSerializer

from sounds.models import Sound


class SoundSerializer(serializers.ModelSerializer):
    """Serializer for sound model."""
    profile = ProfileSerializer()

    class Meta:
        model = Sound
        fields = ('name', 'profile', 'sound_file', 'first_video', 'copyright')
