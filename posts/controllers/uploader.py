from base.utils import (
    get_ip_address,
    get_ip_details
)

from posts.models import Post, PostCategory

from sounds.models import Sound

from tag.controllers.tag_central import TagCentral

from tracker.models import PostLocation


class PostUploader:
    """Handle post upload."""

    @staticmethod
    def handle_location(request):
        """Handle location from where post was uploaded."""
        ip_address = get_ip_address(request)
        if ip_address:
            location = get_ip_details(ip_address)
            try:
                PostLocation.objects.create(
                    ip_address=ip_address,
                    state=location.get('region'),
                    country=location.get('country_name'),
                    latitude=location.get('latitude'),
                    longitude=location.get('longitude'),
                    postal_code=location.get('postal'),
                    city=location.get('city')
                )
            except BaseException:
                return False
        return True

    def upload(self, user, file, details, request):
        """Upload a post in model."""
        try:
            original_post = category = None
            if details.get('share_post_uuid', None):
                original_post = Post.objects.get(uuid=details.get('share_post_uuid'))
            if details.get('category', None):
                category = PostCategory.objects.get(name=details.get('category', None))
            post = Post.objects.create(
                profile=user.profile,
                video_file=file['video_file'],
                video_gif=file['video_gif'],
                description=details.get('description', None),
                sound=Sound.objects.get(uuid=details.get('sound_uuid')),
                share_pointer=original_post,
                category=category,
                is_pornographic=details.get('is_pornographic', False)
            )
            is_tags_added = TagCentral().handle_tag_cycle(post)
            is_location_added = self.handle_location(request)
            return {
                'message': ('Post successfully Uploaded, '
                            'hashtags added {},'
                            'location added {}').format(
                    is_tags_added,
                    is_location_added
                )
            }
        except BaseException as e:
            return {'message': 'Error Occured: {}'.format(e)}
