"""Handle all documentation related functions."""
from django.urls import path
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Misco API",
      default_version='v1',
      description=('All the APIs are documented here. This application covers all important aspects '
                   'of audio/video and can be termed as an enhanced clone of Tiktok. This project'
                   'is completely maintained by Chayan Datta.'),
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="chayandatta007@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

url_patterns = [
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
