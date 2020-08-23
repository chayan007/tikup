from posts.models import Post, PostCategory

from sounds.models import Sound

from tag.controllers.tag_central import TagCentral


class PostUploader:
    """Handle post upload."""

    @staticmethod
    def upload(user, file, details):
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
            return {'message': 'Post succesfully Uploaded, hashtags added {}'.format(is_tags_added)}
        except BaseException as e:
            return {'message': 'Error Occured: {}'.format(e)}
