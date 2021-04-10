# Third Party Library
from django.urls import path

# Application Library
from chat_scheduler.views import (
    MessageView,
    Ping,
)

urlpatterns = [
    path("", MessageView.as_view(), name="process-message"),
    path("ping/", Ping.as_view(), name="ping")
]
