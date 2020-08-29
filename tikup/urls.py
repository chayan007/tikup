from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token

from tikup.documentation import url_patterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('usermodule.urls'), name='users'),
    path('sounds/', include('sounds.urls'), name='sounds'),
    path('posts/', include('posts.urls'), name='posts'),
    path('tags/', include('tag.urls'), name='tags'),
    path('activities/', include('activity.urls'), name='activities'),
    path('notifications/', include('notifications.urls'), name='notifications'),
    path('favorites/', include('favorites.urls'), name='favorites'),
    path('timeline/', include('timeline.urls'), name='timeline'),
    path('auth/token/', obtain_auth_token, name='api_token_auth')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + doc_urls
