"""Common URLs for posts application."""
from django.urls import path

from activity.api.views import PostCommentView, PostLikeView, PostReportView

urlpatterns = [
    path('api/comment/', PostCommentView.as_view(), name='comment'),
    path('api/like/', PostLikeView.as_view(), name='like'),
    path('api/report/', PostReportView.as_view(), name='report'),
]
