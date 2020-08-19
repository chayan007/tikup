from sounds.models import Sound


class SoundUploader:
    """Handle sound upload."""

    @staticmethod
    def upload(user, file, details):
        """Upload a sound in model."""
        try:
            Sound.objects.create(
                name=details.get('name', None),
                profile=user.profile,
                sound_file=file['sound_file'],
                category__name=details.get('category', None)
            )
            return {'message': 'Succesfully Uploaded'}
        except BaseException as e:
            return {'message': 'Error Occured: {}'.format(e)}
