from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from chat_scheduler.models import Chat


class ChatSerializer(serializers.ModelSerializer):
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
