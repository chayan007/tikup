from django.contrib import admin

from activity.models import Activity, Comment, CommentLike

admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(CommentLike)
