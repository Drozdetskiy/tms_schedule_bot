# Third Party Library
from django.urls import path

# Application Library
from chat_scheduler.views import (
    CreateChatView,
    Ping,
    ChatViewSet,
    MessageViewSet,
    CronTabViewSet,
    PeriodicTaskViewSet
)


crontab_list = CronTabViewSet.as_view({
    "get": "list",
    "post": "create"
})

crontab_detail = CronTabViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

message_list = MessageViewSet.as_view({
    "get": "list",
    "post": "create"
})

message_detail = MessageViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

chat_list = ChatViewSet.as_view({
    "get": "list",
})

chat_detail = ChatViewSet.as_view({
    "get": "retrieve",
    "patch": "partial_update",
    "delete": "destroy"
})

periodic_task_list = PeriodicTaskViewSet.as_view({
    "get": "list",
    "post": "create"
})

periodic_task_detail = PeriodicTaskViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("", CreateChatView.as_view(), name="process-message"),
    path("chats/", chat_list, name="chats"),
    path("chats/<int:pk>/", chat_detail, name="chat"),
    path("messages/", message_list, name="messages"),
    path("messages/<int:pk>/", message_detail, name="message"),
    path("crontabs/", crontab_list, name="crontabs"),
    path("crontabs/<int:pk>/", crontab_detail, name="crontab"),
    path("periodic_tasks/", periodic_task_list, name="periodic_tasks"),
    path(
        "periodic_tasks/<int:pk>/",
        periodic_task_detail,
        name="periodic_task",
    ),
    path("ping/", Ping.as_view(), name="ping"),
]
