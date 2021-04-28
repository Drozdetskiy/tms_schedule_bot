# Standard Library
import logging
import time
from dataclasses import asdict
from typing import Any

# Third Party Library
from django.conf import settings
from django_celery_beat.models import (
    CrontabSchedule,
    PeriodicTask,
)
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response

# Third Party Library
from rest_framework.views import APIView

# Application Library
from rest_framework.viewsets import ModelViewSet

from chat_scheduler.serializers import (
    CreateChatSerializer,
    ChatSerializer,
    MessageSerializer,
    CrontabSerializer,
    PeriodicTaskSerializer,
)
from chat_scheduler.models import Chat, Message as MessageModel
from chat_scheduler.telegram_logic.callbacks import event_success_callback
from chat_scheduler.telegram_logic.message import Message

__all__ = (
    "CreateChatView",
    "Ping",
    "ChatViewSet",
    "MessageViewSet",
    "CronTabViewSet",
    "PeriodicTaskViewSet",
)

logger = logging.getLogger(f"{settings.PROJECT}")


class CreateCallbackMixin:
    success_callback: Any = None

    def perform_create(self, serializer):
        super().perform_create(serializer)
        if settings.ENABLE_MESSAGE_CALLBACK:
            self.success_callback(serializer.data)


class TelegramPostMixin:
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as exc:
            logger.error(f"Error with message {request.data} with exc: {exc}")
        return Response(status=status.HTTP_200_OK)


class CreateChatView(TelegramPostMixin, CreateCallbackMixin, CreateAPIView):
    serializer_class = CreateChatSerializer
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


class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = MessageModel.objects.all()


class CronTabViewSet(ModelViewSet):
    serializer_class = CrontabSerializer
    queryset = CrontabSchedule.objects.all()


class PeriodicTaskViewSet(ModelViewSet):
    serializer_class = PeriodicTaskSerializer
    queryset = PeriodicTask.objects.all()
