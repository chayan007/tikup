from posts.models import Post


class PostUploader:
    """Handle sound upload."""

    @staticmethod
    def upload(user, file, details):
        """Upload a post in model."""
        try:
            Post.objects.create(
                profile=user.profile,
                video_file=file['video_file'],
                video_gif=file['video_gif'],
                description=details.get('description', None),
                sound__uuid=details.get('sound_uuid', None),
                share_pointer__uuid=details.get('share_post_uuid', None)
            )
            return {'message': 'Succesfully Uploaded'}
        except BaseException as e:
            return {'message': 'Error Occured: {}'.format(e)}
