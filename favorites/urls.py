"""Common URLs for favorites application."""
from django.urls import path

from favorites.api.views import FavoriteView, UserInterestView

urlpatterns = [
    path('api/interest/', UserInterestView.as_view(), name='interest'),
    path('api/<model_marker>/', FavoriteView.as_view(), name='list'),
    path('api/<model_marker>/<object_id>', FavoriteView.as_view(), name='mark'),
]
