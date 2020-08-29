from django.contrib import admin

from tracker.models import PostLocation

@admin.register(PostLocation)
class PostLocationAdmin(admin.ModelAdmin):
    """Admin for tracking posts."""

    list_display = ('ip_address', 'city', 'state', 'country')