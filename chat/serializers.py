from django.db import IntegrityError
from rest_framework import serializers
from .models import Messages


class MessagesSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_pic.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Messages
        fields = [
            'id', 'owner', 'message', 'created_at',
            'profile_id', 'profile_image', 'is_owner', 'profile'
        ]


class MessagesDetailSerializer(MessagesSerializer):
    """
    Serializer for the Contact model used in Detail view
    profile is a read only field so that we dont have to set it on each update
    """
    profile = serializers.ReadOnlyField(source='profile.id')
