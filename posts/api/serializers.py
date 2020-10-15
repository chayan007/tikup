from rest_framework import serializers

from activity.utils import post_views_count

from favorites.utils import is_post_favorite

from posts.utils import comments_count, likes_count, share_count

from sounds.api.serializers import SoundSerializer

from usermodule.api.serializers import ProfileSerializer

from posts.models import Post, PostCategory


class PostCategorySerializer(serializers.ModelSerializer):
    """Serializer for post category model."""

    class Meta:
        model = PostCategory
        fields = ('uuid', 'name', 'icon', 'description')


class PostSerializer(serializers.ModelSerializer):
    """Serializer for post model."""
    profile = ProfileSerializer()
    sound = SoundSerializer()
    category = PostCategory()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    shares = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    is_viewed = serializers.SerializerMethodField()

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if not request:
            return False
        return is_post_favorite(
            request.user.profile,
            obj
        )

    def get_is_viewed(self, obj):
        request = self.context.get('request')
        if not request:
            return False
        return is_post_favorite(
            request.user.profile,
            obj
        )

    def get_likes(self, obj):
        return likes_count(obj)

    def get_comments(self, obj):
        return comments_count(obj)

    def get_shares(self, obj):
        return share_count(obj)

    def get_views(self, obj):
        return post_views_count(obj)

    class Meta:
        model = Post
        fields = (
            'uuid', 'profile', 'sound', 'video_file',
            'video_gif', 'description', 'category',
            'likes', 'shares', 'comments', 'views',
            'is_favorite', 'is_downloadable'
        )
