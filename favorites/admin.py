from django.contrib import admin

from favorites.models import FavoritePost, FavoriteSound, UserInterest


admin.site.register(FavoritePost)
admin.site.register(FavoriteSound)
admin.site.register(UserInterest)
