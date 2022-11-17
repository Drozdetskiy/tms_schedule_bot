# Third Party Library
from django_celery_beat.models import (
    CrontabSchedule,
    PeriodicTask,
)
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

# Application Library
from chat_scheduler.models import (
    Chat,
    Message,
)


class CreateChatSerializer(serializers.ModelSerializer):
    chat_id = serializers.IntegerField()

    class Meta:
        model = Chat
        fields = ("chat_id", )

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, UniqueTogetherValidator):
                self.validators.remove(validator)
        super().run_validators(value)

    def create(self, validated_data):
        instance, _ = self.Meta.model.objects.get_or_create(**validated_data)
        return instance


class ChatSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)

    class Meta:
        model = Chat
        fields = ("pk", "chat_id", "name", "updated_at")


class MessageSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=30)
    message_text = serializers.CharField()

    class Meta:
        model = Message
        fields = ("pk", "title", "message_text", "updated_at")


class CrontabSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    minute = serializers.CharField(max_length=60 * 4, required=False)
    hour = serializers.CharField(max_length=24 * 4, required=False)
    day_of_week = serializers.CharField(max_length=64, required=False)
    day_of_month = serializers.CharField(max_length=31 * 4, required=False)
    month_of_year = serializers.CharField(max_length=64, required=False)

    class Meta:
        model = CrontabSchedule
        fields = (
            "pk",
            "name",
            "minute",
            "hour",
            "day_of_week",
            "day_of_month",
            "month_of_year",
        )

    @classmethod
    def get_name(cls, obj: CrontabSchedule) -> str:
        return str(obj)


class PeriodicTaskSerializer(MessageSerializer):
    name = serializers.CharField(max_length=200)
    args = serializers.CharField()
    crontab_id = serializers.IntegerField()
    task = serializers.CharField(max_length=200)

    class Meta:
        model = PeriodicTask
        fields = ("pk", "name", "task", "crontab_id", "args")
