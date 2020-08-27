"""Common URLs for posts application."""
from django.urls import path

from activity.api.views import PostCommentView, PostLikeView, PostReportView

urlpatterns = [
    path('api/comment/<post_id>', PostCommentView.as_view(), name='comment'),
    path('api/like/<post_id>', PostLikeView.as_view(), name='like'),
    path('api/report/<post_id>', PostReportView.as_view(), name='report'),
]
