from django.contrib import admin

from tag.models import Hashtag, HashtagLink

admin.site.register(Hashtag)
admin.site.register(HashtagLink)
