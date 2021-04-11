# Third Party Library
from celery import shared_task


@shared_task
def send_message(chat_pk: int, message_pk: int):
    # Application Library
    from chat_scheduler.logic import SendMessageCommand
    command = SendMessageCommand(chat_pk, message_pk)
    command.execute()
