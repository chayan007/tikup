"""Common URLs for posts application."""
from django.urls import path, include

from activity.api.views import PostCommentView

urlpatterns = [
    path('api/comment/upload/', PostCommentView.as_view(), name='add_comment')
]
