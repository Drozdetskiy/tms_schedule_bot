# Third Party Library
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Chat(models.Model):
    chat_id = models.BigIntegerField(_("Chat id"), unique=True)
    name = models.CharField(
        _("Chat name"), max_length=30, null=True, blank=True
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )


class Message(models.Model):
    title = models.CharField(_("Title"), max_length=30)
    message_text = models.TextField(_("Message Text"))
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )
