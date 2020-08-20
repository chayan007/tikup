from django.contrib import admin

from posts.models import *
from posts.utils import *


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    """Admin for post Category."""

    list_display = ('name', 'icon', 'description')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin for Post model."""

    def get_likes_count(self, obj):
        return likes_count(obj)

    def get_comments_count(self, obj):
        return comments_count(obj)

    def get_share_count(self, obj):
        return share_count(obj)

    list_display = (
        'profile', 'sound', 'share_pointer',
        'get_likes_count',
        'get_comments_count',
        'get_share_count'
    )
