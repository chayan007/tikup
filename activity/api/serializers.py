"""Serializer for models."""
from rest_framework import serializers

from activity.models import Comment

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
    reply = CommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('uuid', 'profile', 'comment', 'reply', 'created_at')
