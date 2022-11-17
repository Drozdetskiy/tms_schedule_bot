# Standard Library
import logging
from typing import Dict

# Application Library
import settings
from chat_scheduler.telegram_logic.client import TelegramClient

logger = logging.getLogger(f"{settings.PROJECT}")

__all__ = (
    "event_success_callback",
)

SUCCESS_MESSAGE = "Hello! Nice to meet you."


def event_success_callback(data: Dict[str, int]):
    chat_id = data["chat_id"]
    client = TelegramClient(chat_id)
    resp = client.send_message(message=SUCCESS_MESSAGE)
    logger.debug(resp)
