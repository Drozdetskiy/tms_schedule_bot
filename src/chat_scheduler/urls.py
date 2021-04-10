# Third Party Library
from django.urls import path

# Application Library
from chat_scheduler.views import MessageView

urlpatterns = [
    path("", MessageView.as_view(), name="create-event"),
]
