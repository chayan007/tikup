"""Get all timeline related functions."""
from base.utils import get_ip_address, get_ip_details

from posts.models import Post

from usermodule.models import FollowerMap


class TimelineCentral:

    def get_country(self, request):
        """Get country from where user is surfing."""
        ip_address = get_ip_address(request)
        if ip_address or ip_address == '127.0.0.1':
            location = get_ip_details(ip_address)
            return location.country_name

    def posts(self, request):
        """Send all non-pornographic posts."""
        country = self.get_country(request)
        qs = {
            'is_pornographic': False,
        }
        if country:
            qs['uploaded_location__country'] = country
        posts = Post.objects.filter(
            **qs
        ).order_by(
            '-created_at',
        )
        return posts
