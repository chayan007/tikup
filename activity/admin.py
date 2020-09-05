from django.contrib import admin

from activity.models import Activity, Comment, CommentLike, PostView, SoundView

admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(PostView)
admin.site.register(SoundView)
