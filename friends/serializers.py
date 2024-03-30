from rest_framework import serializers
from .models import Friend

class FriendSerializer(serializers.Serializer):
    user = serializers.ReadOnlyField(source='user.username')
    friend = serializers.ReadOnlyField(source='friend.username')

    class Meta:
        model = Friend
        fields = ['id', 'created_at', 'user', 'friend']