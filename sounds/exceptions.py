from base.exceptions import CustomAPIException


class SoundUploadException(CustomAPIException):
    """Raise when sound flow fails."""

    default_detail = 'Sound Upload Failed !'
    default_code = 'sound_upload_failed'
