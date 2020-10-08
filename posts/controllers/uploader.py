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
        if ip_address or ip_address == '127.0.0.1':
            location = get_ip_details(ip_address)
            try:
                loc = PostLocation.objects.create(
                    ip_address=ip_address,
                    state=location.region,
                    country=location.country_name,
                    latitude=location.latitude,
                    longitude=location.longitude,
                    postal_code=location.postal,
                    city=location.city
                )
                return loc
            except BaseException:
                return

    def upload(self, user, file, details, request):
        """Upload a post in model."""
        try:
            original_post = category = None
            if details.get('share_post_uuid', None):
                original_post = Post.objects.get(
                    uuid=details.get('share_post_uuid')
                )
            if details.get('category', None):
                category = PostCategory.objects.get(
                    name=details.get('category', None)
                )
            sound = None
            if details.get('sound_uuid', None):
                sound = Sound.objects.get(
                    uuid=details.get('sound_uuid', None)
                )
            location = self.handle_location(request)
            is_location_added = True if location else False
            post = Post.objects.create(
                profile=user.profile,
                video_file=file['video_file'],
                video_gif=file['video_gif'],
                description=details.get('description', None),
                sound=sound,
                share_pointer=original_post,
                category=category,
                is_pornographic=details.get('is_pornographic', False),
                is_downloadable=details.get('is_downloadable', False),
                uploaded_location=location
            )
            is_tags_added = TagCentral().handle_tag_cycle(post)
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
