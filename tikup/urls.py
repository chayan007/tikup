from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('users/', include('usermodule.urls'), name='users'),
    path('sounds/', include('sounds.urls'), name='sounds'),
    path('posts/', include('posts.urls'), name='posts'),
    path('tags/', include('tag.urls'), name='tags'),
    path('activities/', include('activity.urls'), name='activities'),
    path('notifications/', include('notifications.urls'), name='notifications'),
    path('auth/token/', obtain_auth_token, name='api_token_auth')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
