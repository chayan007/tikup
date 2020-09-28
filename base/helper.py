from rest_framework import status


def get_status(code):
    """Get the human readable SNAKE_CASE version of a status code."""
    for key, value in status.__dict__.items():
        if not callable(value) and code is value:
            return key.replace("HTTP_%s_" % code, "")
    return "Unknown"

def modify_response(response):
    """
    Modify API response format.
    """
    if status.is_client_error(response.status_code) or status.is_server_error(
        response.status_code
    ):
        return response

    # Modify the response data
    modified_data = {}
    modified_data["code"] = response.status_code
    modified_data["status"] = get_status(response.status_code)
    modified_data["data"] = response.data

    response.data = modified_data
    return response