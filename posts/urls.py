"""Common URLs for posts application."""
from django.urls import path, include

from posts.api import router
from posts.api.views import (
    SoundBasedPostView,
    PostUploadView,
    PostSearchView,
    PostMetricsView
)

urlpatterns = [
    path('api/models/', include(router.urls)),
    path('api/upload/', PostUploadView.as_view(), name='upload_post'),
    path('api/search/', PostSearchView.as_view(), name='search_post'),
    path('api/metrics/<indicator>/<post_id>', PostMetricsView.as_view(), name='post_metrics'),
    path('api/sound/<sound_id>', SoundBasedPostView.as_view(), name='post_by_sound')
]
