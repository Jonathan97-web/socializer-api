from rest_framework import serializers
from .models import Notes


class NoteskSerializer(serializers.ModelSerializer):
    """Serializer for the Notes model."""
    class Meta:
        model = Notes
        fields = [
            'id',
            'created_at',
            'title',
        ]


class NotesDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Notes model."""
    class Meta:
        model = Notes
        fields = [
            'id',
            'created_at',
            'title',
        ]
