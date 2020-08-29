"""Get all base utils required for this project."""
import ipinfo
from django.conf import settings


def get_ip_address(request):
    """Get IP address from request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_ip_details(ip_address=None):
    """Get location based information from IP Address."""
	ip_info_token = getattr(settings, "IPINFO_TOKEN", None)
	ip_info_settings = getattr(settings, "IPINFO_SETTINGS", {})
    ip_data = ipinfo.getHandler(
        ip_info_token,
        **ip_info_settings
    ).getDetails(ip_address)
    return ip_data
