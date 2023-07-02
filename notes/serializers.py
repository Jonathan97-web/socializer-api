from rest_framework import serializers
from .models import Notes


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Notes model."""
    class Meta:
        model = Task
        fields = [
            'id',
            'created_at',
            'title',
        ]


class TaskDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Notes model."""
    class Meta:
        model = Task
        fields = [
            'id',
            'created_at',
            'title',
        ]
