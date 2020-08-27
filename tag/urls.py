"""URL routes for tag application."""
from django.urls import path, include

from tag.api.views import HashtagSearchView

urlpatterns = [
    path('api/search', HashtagSearchView.as_view(), name='search_hashtags')
]