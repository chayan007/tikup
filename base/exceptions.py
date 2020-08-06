"""Exceptions in Misco application."""
from rest_framework import status
from rest_framework.exceptions import APIException


class CustomAPIException(APIException):
    """Custom API Exception."""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'An unknown API Exception occurred.'
    default_code = 'unknown_api_error'

    def __init__(self, message=None, error_dict=None, code=None,
                 status_code=None):
        """Initialize custom API exception."""
        message = _(message or self.default_detail)
        self.code = code or self.default_code
        self.status_code = status_code or self.status_code

        super(CustomAPIException, self).__init__(detail=message,
                                                 code=self.code)
        self.message = message
        self.error_dict = error_dict or {}
