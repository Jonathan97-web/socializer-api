from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    """Serializer for the Notes model."""
    class Meta:
        model = Notes
        fields = [
            'id',
            'created_at',
            'title',
            'content',
            'owner',
            'is_owner',
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


class NotesDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Notes model."""
    class Meta:
        model = Notes
        fields = [
            'id',
            'created_at',
            'title',
            'content,',
            'owner',
            'is_owner',
        ]
