"""Common URLs for favorites application."""
from django.urls import path

from favorites.api.views import FavoriteView

urlpatterns = [
    path('api/<model_marker>/', FavoriteView.as_view(), name='list'),
    path('api/<model_marker>/<object_id>', FavoriteView.as_view(), name='mark'),
]
