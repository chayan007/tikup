"""Common URLs for sounds application."""
from django.urls import path, include

from sounds.api import router
from sounds.api.views import SoundUploadView, SoundSearchView

urlpatterns = [
    path('api/models/', include(router.urls)),
    path('api/sound/upload/', SoundUploadView.as_view(), name='upload_sound'),
    path('api/search/', SoundSearchView.as_view(), name='sound_search')
]
