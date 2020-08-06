from rest_framework import serializers

from sounds.api.serializers import SoundSerializer

from usermodule.api.serializers import ProfileSerializer

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for post model."""
    profile = ProfileSerializer()
    sound = SoundSerializer()

    class Meta:
        model = Post
        fields = ('profile', 'sound', 'video_file', 'video_gif', 'description')
