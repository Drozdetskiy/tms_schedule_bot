# Standard Library
from typing import Dict

# Application Library
from chat_scheduler.telegram_logic.client import TelegramClient

__all__ = (
    "event_success_callback",
)

SUCCESS_MESSAGE = "Hello! Great to here you"


def event_success_callback(data: Dict[int, int]):
    chat_id = data["chat_id"]  # type: ignore
    client = TelegramClient(chat_id)
    client.send_message(message=SUCCESS_MESSAGE)
