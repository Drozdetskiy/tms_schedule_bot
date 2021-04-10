from django.db import models
from django.utils.translation import ugettext_lazy as _


class Chat(models.Model):
    chat_id = models.IntegerField(_("Chat id"), unique=True)
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )
