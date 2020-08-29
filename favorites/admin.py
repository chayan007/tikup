from django.contrib import admin

from favorites.models import FavoritePost, FavoriteSound


admin.site.register(FavoritePost)
admin.site.register(FavoriteSound)
