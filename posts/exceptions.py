from base.exceptions import CustomAPIException


class PostUploadException(CustomAPIException):
    """Raise when post upload flow fails."""

    default_code = 'post_upload_failure'
    default_detail = 'Post Upload Failed.'
