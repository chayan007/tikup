"""Add all API routes."""
from rest_framework import routers

from django.urls import path, include

from .views import *


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'message', ConversationMessageViewSet, basename='message')
router.register(r'block', BlockedUserViewSet, basename='block')
router.register(r'', ConversationViewSet, basename='conversation')


urlpatterns = [
    path('', include(router.urls)),
]
