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
        fields = ('post', 'profile', 'comment')


class NestedCommentSerializer(serializers.ModelSerializer):
    """Serializer for comment class along with replies."""

    post = PostSerializer()
    profile = ProfileSerializer()
    reply = CommentSerializer()

    class Meta:
        model = Comment
        fields = ('post', 'profile', 'comment', 'reply')
