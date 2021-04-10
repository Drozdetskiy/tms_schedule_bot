# Third Party Library
import logging
import time
from dataclasses import asdict
from typing import Any

from django.conf import settings
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

__all__ = (
    "MessageView",
)

from rest_framework.views import APIView

from chat_scheduler.serializers import ChatSerializer
from chat_scheduler.telegram_logic.callbacks import event_success_callback
from chat_scheduler.telegram_logic.message import Message

logger = logging.getLogger(f"{settings.PROJECT}")


class CreateCallbackMixin:
    success_callback: Any = None

    def perform_create(self, serializer):
        super().perform_create(serializer)
        self.success_callback(serializer.data)


class TelegramPostMixin:
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as exc:
            print(exc)
            logger.error(f"Error with message {request.data}")
        return Response(status=status.HTTP_200_OK)


class MessageView(TelegramPostMixin, CreateCallbackMixin, CreateAPIView):
    serializer_class = ChatSerializer
    success_callback = staticmethod(event_success_callback)

    def create(self, request, *args, **kwargs):
        message = Message(request.data)
        if message.chat_id:
            serializer = self.get_serializer(data=asdict(message))
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        else:
            return Response(status=status.HTTP_200_OK)


class Ping(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            f"pong {time.time()}",
            status=status.HTTP_200_OK,
        )
