from django.db import IntegrityError
from rest_framework import serializers
from .models import Messages, Chat


class ChatSerializer(serializers.ModelSerializer):
    """
    Serializer for the Chat model
    """
    user1 = serializers.ReadOnlyField(source='user1.username')
    user2 = serializers.ReadOnlyField(source='user2.username')

    class Meta:
        model = Chat
        fields = ['id', 'user1', 'user2', 'created_at', 'updated_at']


class ChatDetailSerializer(ChatSerializer):
    """
    Serializer for the Chat model used in Detail view
    """
    user1 = serializers.ReadOnlyField(source='user1.username')
    user2 = serializers.ReadOnlyField(source='user2.username')


class MessagesSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url')

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
    Serializer for the Messages model used in Detail view
    profile is a read only field so that we dont have to set it on each update
    """
    profile = serializers.ReadOnlyField(source='profile.id')
