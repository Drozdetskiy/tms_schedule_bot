# Third Party Library
from django.contrib import admin

# Application Library
# Register your models here.
from chat_scheduler.models import (
    Chat,
    Message,
)


class ChatAdmin(admin.ModelAdmin):
    list_display = (
        "chat_id",
        "name",
        "pk",
        "created_at",
        "updated_at",
    )

    def get_readonly_fields(self, request, obj=None):
        return [
            field.name for field in self.model._meta.fields
        ]

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "message_text",
        "pk",
        "created_at",
        "updated_at",
    )


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
