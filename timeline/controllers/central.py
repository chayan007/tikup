"""Get all timeline related functions."""
from base.utils import get_ip_address, get_ip_details

from favorites.models import UserInterest

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
        categories_selected = UserInterest.objects.filter(
            profile=request.user.profile
        ).values_list(
            'category__uuid', flat=True
        )
        following_uuids = FollowerMap.objects.filter(
            follower=request.user.profile
        ).values_list(
            'profile__uuid', flat=True
        )
        qs = {
            'is_pornographic': False,
        }
        if country:
            qs['uploaded_location__country'] = country
        follower_posts = Post.objects.filter(
            category__uuid__in=categories_selected,
            profile__uuid__in=following_uuids,
            **qs
        ).order_by(
            '-created_at',
        )
        posts = follower_posts | Post.objects.all().exclude(
            uuid__in=follower_posts.values_list(
                'uuid', flat=True
            )
        )
        return posts
