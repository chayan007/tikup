from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('usermodule.urls'), name='users'),
    path('auth/token/', obtain_auth_token, name='api_token_auth')
]
