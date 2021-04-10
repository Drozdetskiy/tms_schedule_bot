# Third Party Library
from django.contrib import admin

# Application Library
# Register your models here.
from chat_scheduler.models import Chat


class ChatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chat, ChatAdmin)
