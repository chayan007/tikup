"""Common URLs for sounds application."""
from django.urls import path, include

from sounds.api import router
from sounds.api.views import (
    SoundCategorySearch,
    SoundUploadView,
    SoundSearchView,
    TrendingSoundCategorisedView
)

urlpatterns = [
    path('api/models/', include(router.urls)),
    path('api/upload/', SoundUploadView.as_view(), name='upload_sound'),
    path('api/search/', SoundSearchView.as_view(), name='sound_search'),
    path('api/category/<category_id>', SoundCategorySearch.as_view(), name='sound_category_filter'),
    path('api/trending/', TrendingSoundCategorisedView.as_view(), name='trending')
]
