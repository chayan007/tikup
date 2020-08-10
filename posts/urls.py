"""Common URLs for posts application."""
from django.urls import path, include

from posts.api import router
from posts.api.views import PostUploadView

urlpatterns = [
    path('api/models/', include(router.urls)),
    path('api/upload/', PostUploadView.as_view(), name='upload_post')
]
