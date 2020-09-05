"""Common URLs for posts application."""
from django.urls import path

from activity.api.views import (
    IncrementPostView,
    IncrementSoundView,
    LikeCommentView,
    PostCommentView,
    PostLikeView,
    PostReportView,
    PostReplyView
)

urlpatterns = [
    path('api/comment/<post_id>', PostCommentView.as_view(), name='comment'),
    path('api/comment/like/<comment_id>', LikeCommentView.as_view(), name='like_comment'),
    path('api/reply/<comment_id>', PostReplyView.as_view(), name='reply'),
    path('api/like/<post_id>', PostLikeView.as_view(), name='like'),
    path('api/report/<post_id>', PostReportView.as_view(), name='report'),
    path('api/view/sound/<sound_id>', IncrementSoundView.as_view(), name='sound_view'),
    path('api/view/post/<post_id>', IncrementPostView.as_view(), name='post_view'),
]
