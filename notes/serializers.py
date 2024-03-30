from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Notes
        fields = [
            'id', 'owner', 'is_owner',
            'created_at', 'updated_at',
            'title', 'content'
        ]
