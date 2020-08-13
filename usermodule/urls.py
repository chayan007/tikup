"""Common URLs for usermodule application."""
from django.urls import path, include

from usermodule.api import router, views


urlpatterns = [
    path('api/models/', include(router.urls)),
    path('register/', views.create_auth, name='register'),
    path('follow/', views.FollowerRequestView.as_view(), name='follow')
]
