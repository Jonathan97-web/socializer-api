from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    """Serializer for the Notes model."""
    class Meta:
        model = Notes
        fields = [
            'id',
            'created_at',
            'title',
            'notes,'
            'owner',
        ]


class NotesDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Notes model."""
    class Meta:
        model = Notes
        fields = [
            'id',
            'created_at',
            'title',
            'notes,',
            'owner',
        ]
