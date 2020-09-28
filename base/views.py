from rest_framework import viewsets
from .helper import modify_response

class ViewSet(viewsets.ViewSet):
    """
    Overriding : Modify the API response format for common place.
    """

    def initial(self, request, *args, **kwargs):
        return super().initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        response = modify_response(response)
        return super().finalize_response(request, response, *args, **kwargs)

    def get_serializer_context(self):
        """
        Set client IP Address and request url in the context
        """
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
