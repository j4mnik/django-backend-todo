from unittest.util import _MAX_LENGTH
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=255)
    importance = serializers.CharField(max_length=25)
    created_at = serializers.DateTimeField()
