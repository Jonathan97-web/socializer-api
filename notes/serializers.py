from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    """Serializer for the Notes model."""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Notes
        fields = [
            'id',
            'created_at',
            'title',
            'owner',
            'is_owner'
        ]


class NotesDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Notes model."""
    class Meta:
        model = Notes
        fields = [
            'id',
            'created_at',
            'title',
            'owner',
            'is_owner'
        ]
