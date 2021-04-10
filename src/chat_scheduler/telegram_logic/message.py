from dataclasses import (
    dataclass,
    InitVar,
    field,
)


@dataclass
class Message:
    message: InitVar[dict]

    chat_id: int = field(init=False)

    def __post_init__(self, message: dict):
        raw_message = message.get("message", {})
        self.chat_id = raw_message.get("chat", {}).get("id")
