from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source="actor.username", read_only=True)
    recipient_username = serializers.CharField(source="recipient.username", read_only=True)

    # “target” is generic, so we expose a lightweight description
    target_type = serializers.SerializerMethodField()
    target_id = serializers.IntegerField(source="target_object_id", read_only=True)

    class Meta:
        model = Notification
        fields = [
            "id",
            "recipient",
            "recipient_username",
            "actor",
            "actor_username",
            "verb",
            "target_type",
            "target_id",
            "is_read",
            "timestamp",
        ]
        read_only_fields = ["id", "recipient", "actor", "timestamp", "target_type", "target_id"]

    def get_target_type(self, obj):
        return obj.target_content_type.model if obj.target_content_type else None