"""Common URLs for posts application."""
from django.urls import path, include

from sounds.api.views import SoundExtractorView

from posts.api import router
from posts.api.views import (
    SoundBasedPostView,
    PostUploadView,
    PostSearchView,
    PostMetricsView,
    TagFilteredPostView,
    TrendingTagPostView,
    UserLikedPostView,
    UserPostView
)

urlpatterns = [
    path('api/models/', include(router.urls)),
    path('api/upload/', PostUploadView.as_view(), name='upload_post'),
    path('api/search/', PostSearchView.as_view(), name='search_post'),
    path('api/metrics/<indicator>/<post_id>', PostMetricsView.as_view(), name='post_metrics'),
    path('api/sound/<sound_id>', SoundBasedPostView.as_view(), name='post_by_sound'),
    path('api/tag/<tag>', TagFilteredPostView.as_view(), name='post_by_tag'),
    path('api/posts/liked/<username>', UserLikedPostView.as_view(), name='user_liked_posts'),
    path('api/posts/<username>', UserPostView.as_view(), name='user_posts'),
    path('api/trending/', TrendingTagPostView.as_view(), name='trending_posts'),
    path('api/extract/<post_uuid>', SoundExtractorView.as_view(), name='extractor')
]
