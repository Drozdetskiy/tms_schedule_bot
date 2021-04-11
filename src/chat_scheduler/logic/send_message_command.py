# Standard Library
import logging

# Third Party Library
from django.conf import settings

# Application Library
from chat_scheduler.models import (
    Chat,
    Message,
)
from chat_scheduler.telegram_logic.client import TelegramClient

__all__ = (
    "SendMessageCommand",
)

logger = logging.getLogger(settings.PROJECT)


class SendMessageCommand:
    def __init__(self, chat_pk: int, message_pk: int):
        self.chat_pk = chat_pk
        self.message_pk = message_pk

    def _send_message(self):
        chat = Chat.objects.get(pk=self.chat_pk)
        message = Message.objects.get(pk=self.message_pk)
        client = TelegramClient(chat.chat_id)
        client.send_message(message=message.message_text)

    def execute(self) -> bool:
        try:
            self._send_message()
        except Exception as exc:
            error = f"Can't send message to chat {self.chat_pk} with " \
                    f"message pk: {self.message_pk}. Reason: {exc}"
            logger.error(error)

            return False

        logger.info(
            f"Send message to chat {self.chat_pk} "
            f"with message pk {self.message_pk}"
        )

        return True
