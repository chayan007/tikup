from django.contrib.auth.models import User

from .models import BlockedUser

from django.db.models import Q


def is_blocked(block_user, user):
    """
    :block_user  : receiver
    :user        : sender
    """
    if block_user == user:
        # same user are not then blocked.
        return False

    try:
        return BlockedUser.objects.filter(
            Q(block_user=block_user, user=user) | Q(
                block_user=user, user=block_user)
        ).exists()
    except BlockedUser.DoesNotExist:
        return False
