"""Common URLs for posts application."""
from django.urls import path

from activity.api.views import PostCommentView

urlpatterns = [
    path('api/comment/', PostCommentView.as_view(), name='comment'),
    path('api/like/', PostCommentView.as_view(), name='like'),
    path('api/report/', PostCommentView.as_view(), name='report'),
]
