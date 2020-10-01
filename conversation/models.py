"""Models for the conversation app."""
import os

from base.models import BaseModel
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Conversation(BaseModel):
    """
    Model to contain different messages between one or more users.
    """

    sender = models.ForeignKey(
        User,
        verbose_name=_("Sender"),
        related_name="Sender",
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        User,
        verbose_name=_("Receiver"),
        related_name="Receiver",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-pk",)
        verbose_name = _("Conversation")
        verbose_name_plural = _("Conversations")

    def __str__(self):
        return "{}".format(self.pk)


class Message(BaseModel):
    """
    Model, which holds information about a post within one conversation.
    :user: User, who posted the message.
    :conversation: Conversation, which contains this message.
    :text: Message text.
    """

    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        related_name="messages",
        on_delete=models.CASCADE
    )

    conversation = models.ForeignKey(
        Conversation,
        verbose_name=_("Conversation"),
        related_name="messages",
        on_delete=models.CASCADE
    )

    text = models.TextField(
        max_length=4096,
        verbose_name=_("Text"),
    )

    is_read = models.BooleanField(
        verbose_name=_("Is read"),
        default=False
    )

    is_delete = models.BooleanField(
        verbose_name=_("Is delete"),
        default=False
    )

    attachment = models.FileField(
        upload_to="attachment",
        verbose_name=_("Attachment"),
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return self.user.email

    def filename(self):
        if self.attachment:  # pragma: nocover
            return os.path.basename(self.attachment.name)
        return ""


class BlockedUser(BaseModel):
    """
    Model to mark a user relationship as blocked.
    :user: Blocked user.
    :blocked_by: User who blocked the other one.
    :date: Date, the user has been blocked.
    """

    user = models.ForeignKey(
        User,
        verbose_name=_("Blocked user"),
        related_name="blocked",
        on_delete=models.CASCADE
    )

    block_user = models.ForeignKey(
        User,
        verbose_name=_("Blocked User"),
        related_name="blocked_users",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Blocked user")
        verbose_name_plural = _("Blocked users")

    def __str__(self):
        return self.user.email
