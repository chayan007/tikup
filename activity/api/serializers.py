"""Serializer for models."""
from rest_framework import serializers

from activity.models import Comment, CommentLike

from posts.api.serializers import PostSerializer

from usermodule.api.serializers import ProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    """Serializer class for comment model."""

    post = PostSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = Comment
        fields = ('post', 'profile', 'comment', 'created_at')


class NestedCommentSerializer(serializers.ModelSerializer):
    """Serializer for comment class along with replies."""

    profile = ProfileSerializer()
    is_pointed_to = CommentSerializer(many=True)
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        """Return count of likes."""
        return CommentLike.objects.filter(
            comment=obj
        ).count()

    class Meta:
        model = Comment
        fields = ('uuid', 'profile', 'comment',
                  'is_pointed_to', 'likes', 'created_at')
