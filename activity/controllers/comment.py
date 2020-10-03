"""Handle comment related functions."""
import re

from django.contrib.auth.models import User

from notifications.models import Notification


class CommentParser:
    """Parse comments and manage flow."""

    def __init__(self, commenter):
        self.commenter = commenter

    def _notify_users(self, usernames):
        """Notify all usernames."""
        for username in usernames:
            try:
                Notification.objects.create(
                    profile=User.objects.get(username=username).profile,
                    message='{} has replied to your comment.'.format(
                        self.commenter.user.profile.user.username
                    ),
                    category=Notification.NotificationCategory.PUSH.value
                )
            except BaseException:
                continue

    def parse_and_notify(self, comment):
        """Parse the comment."""
        if '@' not in comment:
            return
        usernames = re.findall("[@]\\w+", comment)
        self._notify_users(usernames)
